from django.urls import path

from .views import *

app_name = 'rechat'
urlpatterns = [
    path('chats/', Chats.as_view()),
    path('dialog/', Dialog.as_view()),
    path('users/', AddUsersRoom.as_view()),
    ]