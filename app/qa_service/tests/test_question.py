import pytest

from django.urls import reverse
from rest_framework.test import APIClient

from qa_service.models import CustomUser, Question



@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db) -> CustomUser:
    return CustomUser.objects.create_user(username="testuser", password="pass1234")


@pytest.fixture
def question(db) -> Question:
    return Question.objects.create(text="Тестовый вопрос")


def test_get_questions_list(api_client, question):
    url = reverse("question-list")
    response = api_client.get(url)
    assert response.status_code == 200
    assert any(item["id"] == question.id for item in response.json())


def test_create_question_authenticated(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse("question-list")
    data = {"text": "Новый вопрос"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.json()["text"] == "Новый вопрос"


def test_create_question_unauthenticated(api_client):
    url = reverse("question-list")
    data = {"text": "Новый вопрос"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == 403


def test_get_question_detail(api_client, question):
    url = reverse("question-detail", kwargs={"id": question.id})
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json()["id"] == question.id


def test_delete_question(api_client, user, question):
    api_client.force_authenticate(user=user)
    url = reverse("question-detail", kwargs={"id": question.id})
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not Question.objects.filter(id=question.id).exists()
