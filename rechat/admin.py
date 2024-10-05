from django.contrib import admin
from .models import Message, Chat


@admin.register(Chat)
class RoomAdmin(admin.ModelAdmin):
    """Комнаты чата"""
    list_display = ("doctor", "patient")


@admin.register(Message)
class ChatAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ("chat", "user", "content")