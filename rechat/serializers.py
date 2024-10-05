from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Message, Chat


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")


class ChatSerializers(serializers.ModelSerializer):
    """Сериализация комнат чата"""
    patient = UserSerializer()
    doctor = UserSerializer()

    class Meta:
        model = Chat
        fields = ("id", "patient", "doctor")


class MessageSerializers(serializers.ModelSerializer):
    """Сериализация сообщения"""
    user = UserSerializer()

    class Meta:
        model = Message
        fields = ("user", "content", "time_sent", )


class MessagePostSerializers(serializers.ModelSerializer):
    """Сериализация сообщения"""
    class Meta:
        model = Message
        fields = ("chat", "content")
