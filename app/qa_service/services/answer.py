from typing import Any

from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from qa_service.models import Answer, Question, CustomUser
from qa_service.serializers.answer import AnswerSerializer


class AnswerService:
    def get_answer(self, answer_id: int) -> Response:
        try:
            answer = get_object_or_404(Answer, id=answer_id)
            serializer = AnswerSerializer(answer)
            return Response(serializer.data)
        except Exception:
            return Response({"ошибка": "Ответ не найден"}, status=status.HTTP_404_NOT_FOUND)

    def create_answer(self, question_id: int, user: CustomUser, data: dict[str, Any]) -> Response:
        serializer = AnswerSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        question = get_object_or_404(Question, id=question_id)

        answer = Answer.objects.create(
            question=question,
            user=user,
            text=serializer.validated_data["text"],
        )

        return Response(AnswerSerializer(answer).data,status=status.HTTP_201_CREATED)

    def delete(self, answer_id: int, user: CustomUser) -> Response:
        try:
            answer = get_object_or_404(Answer, id=answer_id)
            if answer.user != user:
                raise PermissionDenied("Вы можете удалять только свои ответы")
            answer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except PermissionDenied as e:
            return Response({"ошибка": str(e)}, status=status.HTTP_403_FORBIDDEN)
        except Exception:
            return Response({"ошибка": "Ответ не найден"}, status=status.HTTP_404_NOT_FOUND)
