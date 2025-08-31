from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from qa_service.services.question import QuestionService


class QuestionListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request: Request) -> Response:
        return QuestionService().get_all_questions()

    def post(self, request: Request) -> Response:
        return QuestionService().create_question(request.data)


class QuestionDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request: Request, id: int) -> Response:
        return QuestionService().get_question_with_answers(id)

    def delete(self, request: Request, id: int) -> Response:
        return QuestionService().delete_question(id)
