from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    patient = models.ForeignKey(User, on_delete=models.PROTECT, related_name='p_chat')
    doctor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='d_chat')  # ???


class Message(models.Model):
    time_sent = models.DateTimeField("Дата отправки", auto_now_add=True)
    #    is_read = models.BooleanField()
    content = models.TextField(max_length=1024)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE,
                             related_name='messages')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='messages')

    class Meta:
        verbose_name = "Сообщение чата"
        verbose_name_plural = "Сообщения чатов"
