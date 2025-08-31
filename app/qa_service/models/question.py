from django.db import models


class Question(models.Model):
    text = models.TextField(
        verbose_name="Текст вопроса",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Вопрос {self.id}: {self.text[:50]}"
