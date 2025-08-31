from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from qa_service.services.answer import AnswerService
from qa_service.models import CustomUser


class AnswerCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request: Request, question_id: int) -> Response:
        user: CustomUser = request.user
        return AnswerService().create_answer(
            question_id=question_id,
            user=user,
            data=request.data,
        )


class AnswerDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request: Request, id: int) -> Response:
        return AnswerService().get_answer(id)

    def delete(self, request: Request, id: int) -> Response:
        user: CustomUser = request.user
        return AnswerService().delete(id, user)
