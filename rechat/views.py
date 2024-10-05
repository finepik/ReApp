from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from django.contrib.auth.models import User

from .models import Message, Chat
from .serializers import (MessageSerializers, ChatSerializers, MessagePostSerializers,  UserSerializer)


class Chats(APIView):
    """Комнаты чата"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        chats = Chat.objects.filter(Q(doctor=request.user) | Q(patient=request.user))
        serializer = ChatSerializers(chats, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        patient_id = self.request.query_params.get('patient_id', None)
        if not patient_id:
            return Response({"error": "Method POST not allowed, not patient_id"})

        try:
            patient = User.objects.get(pk=int(patient_id))
        except:
            return Response({"error": "Patient not found"})
        Chat.objects.create(doctor=request.user, patient=patient)
        return Response(status=201)


class Dialog(APIView):
    """Диалог чата, сообщение"""
    permission_classes = [permissions.IsAuthenticated, ]
    # permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        chat = request.GET.get("room")
        message = Message.objects.filter(chat=chat)
        serializer = MessageSerializers(message, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        # room = request.data.get("room")
        dialog = MessagePostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)


class AddUsersRoom(APIView):
    """Добавление юзеров в комнату чата"""
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        chat = request.data.get("room")
        user = request.data.get("user")
        try:
            chat = Chat.objects.get(id=chat)
            chat.patient.add(user)
            chat.save()
            return Response(status=201)
        except:
            return Response(status=400)
