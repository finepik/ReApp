from datetime import datetime, timedelta

from rest_framework import serializers

from .models import Exercises, TrainingTemplate, Training, Progress


class ExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        # get time from request
        t = validated_data.get('time', instance.time)
        # parse time from str to datetime
        new_time = datetime.strptime(t, "%H:%M:%S")
        # create timedelta from datatime
        delta = timedelta(hours=new_time.hour, minutes=new_time.minute, seconds=new_time.second)
        # save new delta
        instance.time = delta
        instance.number_repeat = validated_data.get('number_repeat', instance.number_repeat)
        instance.save()
        return instance


class TrainingTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingTemplate
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.is_done = validated_data.get('is_done', instance.is_done)
        instance.save()
        return instance


class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = "__all__"


class DetailTrainingSerializer(serializers.ModelSerializer):
    progress = ProgressSerializer(many=True)

    class Meta:
        model = Training
        fields = ("id", "date", "is_done", "training_template", "patient", "progress")
