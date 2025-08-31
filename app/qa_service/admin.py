from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from qa_service.models import CustomUser, Question, Answer


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "created_at")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "user", "text", "created_at")
