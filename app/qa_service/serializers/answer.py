from django.contrib.auth import get_user_model
from rest_framework import serializers

from qa_service.models import Answer


User = get_user_model()

class AnswerSerializer(serializers.ModelSerializer):
    text = serializers.CharField(allow_blank=True)
    question = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        required=False,
    )

    class Meta:
        model = Answer
        fields = ["id", "question", "user", "text", "created_at"]
        read_only_fields = ["id", "user", "created_at"]

    def validate_text(self, value: str) -> str:
        if not value or not value.strip():
            raise serializers.ValidationError("Текст ответа не может быть пустым")
        return value.strip()
