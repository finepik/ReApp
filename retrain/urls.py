from django.urls import path

from .views import ExercisesAPIView, TrainingTemplateAPIView, TrainingAPIView, DetailTrainingAPIView, ProgressAPIView

app_name = 'retrain'
urlpatterns = [
    path('exercises/', ExercisesAPIView.as_view(), name='exercises'),
    path('exercises/<int:pk>/', ExercisesAPIView.as_view(), name='exercises-update'),
    path('template/', TrainingTemplateAPIView.as_view(), name='template'),
    path('template/<int:pk>/', TrainingTemplateAPIView.as_view(), name='template-update'),
    path('training/', TrainingAPIView.as_view(), name='training'),
    path('training/<int:pk>/', DetailTrainingAPIView.as_view(), name='detail-training'),
    path('progress/', ProgressAPIView.as_view(), name='progress'),
]
