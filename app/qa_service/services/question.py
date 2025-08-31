from typing import Any

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from qa_service.models import Question
from qa_service.serializers.question import QuestionBaseSerializer, QuestionWithAnswersSerializer


class QuestionService:
    def get_all_questions(self) -> Response:
        questions = Question.objects.all()
        serializer = QuestionBaseSerializer(questions, many=True)
        return Response(serializer.data)

    def get_question_with_answers(self, question_id: int) -> Response:
        try:
            question = get_object_or_404(Question, id=question_id)
            serializer = QuestionWithAnswersSerializer(question)
            return Response(serializer.data)
        except Exception:
            return Response({"ошибка": "Вопрос не найден"}, status=status.HTTP_404_NOT_FOUND)

    def create_question(self, data: dict[str, Any]) -> Response:
        serializer = QuestionBaseSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        question = Question.objects.create(
            text=serializer.validated_data["text"]
        )
        return Response(QuestionBaseSerializer(question).data, status=status.HTTP_201_CREATED)

    def delete_question(self, question_id: int) -> Response:
        try:
            question = get_object_or_404(Question, id=question_id)
            question.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response({"ошибка": "Вопрос не найден"}, status=status.HTTP_404_NOT_FOUND)
