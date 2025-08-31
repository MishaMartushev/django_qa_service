from rest_framework import serializers

from qa_service.models import Question
from qa_service.serializers.answer import AnswerSerializer


class QuestionBaseSerializer(serializers.ModelSerializer):
    text = serializers.CharField(allow_blank=True)

    class Meta:
        model = Question
        fields = ["id", "text", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_text(self, value: str) -> str:
        if not value or not value.strip():
            raise serializers.ValidationError("Текст вопроса не может быть пустым")
        return value.strip()


class QuestionWithAnswersSerializer(QuestionBaseSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta(QuestionBaseSerializer.Meta):
        fields = QuestionBaseSerializer.Meta.fields + ["answers"]
