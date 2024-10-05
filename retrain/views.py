from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Exercises, TrainingTemplate, Training, Progress
from .serializers import ExercisesSerializer, TrainingTemplateSerializer, TrainingSerializer, ProgressSerializer, \
    DetailTrainingSerializer


class ExercisesAPIView(APIView):
    def get(self, request):
        exercises = Exercises.objects.all()
        return Response({"data": ExercisesSerializer(exercises, many=True).data})

    def post(self, request):
        serializer = ExercisesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data})

    def patch(self, request, *args, **kwargs):
        id_exercises = kwargs.get("pk", None)

        if not id_exercises:
            return Response({"error": "Method PUT not allowed, not id_exercises"})

        try:
            instance = Exercises.objects.get(pk=id_exercises)
        except:
            return Response({"error": "Method PUT not allowed"})

        updated_exercises = ExercisesSerializer().update(validated_data=request.data, instance=instance)
        return Response({"data": ExercisesSerializer(updated_exercises).data})


class TrainingTemplateAPIView(APIView):
    def get(self, request):
        train_temp = TrainingTemplate.objects.all()
        return Response({"data": TrainingTemplateSerializer(train_temp, many=True).data})

    def post(self, request):
        serializer = TrainingTemplateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data})

    def patch(self, request, *args, **kwargs):
        id_template = kwargs.get("pk", None)

        if not id_template:
            return Response({"error": "Method PUT not allowed, not id_template"})

        try:
            instance = TrainingTemplate.objects.get(pk=id_template)
        except:
            return Response({"error": "Method PUT not allowed"})

        updated_template = TrainingTemplateSerializer().update(validated_data=request.data, instance=instance)
        return Response({"data": TrainingTemplateSerializer(updated_template).data})


class TrainingAPIView(APIView):
    def get(self, request):
        train_temp = Training.objects.all()
        return Response({"data": TrainingSerializer(train_temp, many=True).data})

    def post(self, request):
        serializer = TrainingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data})


class DetailTrainingAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method GET not allowed"})

        try:
            training = Training.objects.get(pk=pk)
        except:
            return Response({"error": "Method GET not allowed"})

        return Response({"data": DetailTrainingSerializer(training).data})

    def patch(self, request, *args, **kwargs):
        id_training = kwargs.get("pk", None)

        if not id_training:
            return Response({"error": "Method PUT not allowed, not id_training"})

        try:
            instance = Training.objects.get(pk=id_training)
        except:
            return Response({"error": "Method PUT not allowed"})

        updated_training = TrainingSerializer().update(validated_data=request.data, instance=instance)
        return Response({"data": TrainingSerializer(updated_training).data})


class ProgressAPIView(APIView):
    def get(self, request):
        progress = Progress.objects.all()
        return Response({"data": ProgressSerializer(progress, many=True).data})

    def post(self, request):
        serializer = ProgressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data})
