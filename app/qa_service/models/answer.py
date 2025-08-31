from django.conf import settings
from django.db import models

from qa_service.models.question import Question


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers",
        verbose_name="Вопрос",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="answers",
        verbose_name="Пользователь",
    )
    text = models.TextField(
        verbose_name="Текст ответа",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        ordering = ["created_at"]

    def __str__(self):
        return f"Ответ - {self.id} к вопросу - {self.question.id}"
