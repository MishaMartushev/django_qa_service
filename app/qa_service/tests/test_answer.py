import pytest

from django.urls import reverse
from rest_framework.test import APIClient

from qa_service.models import CustomUser, Question, Answer



@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db) -> CustomUser:
    return CustomUser.objects.create_user(username="answeruser", password="pass1234")


@pytest.fixture
def question(db) -> Question:
    return Question.objects.create(text="Вопрос для ответов")


@pytest.fixture
def answer(db, user, question) -> Answer:
    return Answer.objects.create(question=question, user=user, text="Ответ")


def test_create_answer_authenticated(api_client, user, question):
    api_client.force_authenticate(user=user)
    url = reverse("answer-create", kwargs={"question_id": question.id})
    data = {"text": "Новый ответ"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.json()["text"] == "Новый ответ"


def test_create_answer_unauthenticated(api_client, question):
    url = reverse("answer-create", kwargs={"question_id": question.id})
    data = {"text": "Новый ответ"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == 403


def test_get_answer_detail(api_client, answer):
    url = reverse("answer-detail", kwargs={"id": answer.id})
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json()["id"] == answer.id


def test_delete_answer_by_owner(api_client, user, answer):
    api_client.force_authenticate(user=user)
    url = reverse("answer-detail", kwargs={"id": answer.id})
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not Answer.objects.filter(id=answer.id).exists()


def test_delete_answer_by_other_user(api_client, answer):
    other_user = CustomUser.objects.create_user(username="otheruser", password="pass1234")
    api_client.force_authenticate(user=other_user)
    url = reverse("answer-detail", kwargs={"id": answer.id})
    response = api_client.delete(url)
    assert response.status_code == 403
