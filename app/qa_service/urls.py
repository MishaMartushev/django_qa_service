from django.urls import path

from qa_service.views.answer import AnswerCreateView, AnswerDetailView
from qa_service.views.question import QuestionListView, QuestionDetailView


urlpatterns = [
    path("questions/", QuestionListView.as_view(), name="question-list"),
    path("questions/<int:id>/", QuestionDetailView.as_view(), name="question-detail"),
    path("questions/<int:question_id>/answers/", AnswerCreateView.as_view(), name="answer-create"),
    path("answers/<int:id>/", AnswerDetailView.as_view(), name="answer-detail"),
]
