from django.db import models
from reauth.models import DoctorProfile, PatientProfile


class Exercises(models.Model):
    name = models.CharField(max_length=127)
    time = models.DurationField()
    number_repeat = models.IntegerField()


class TrainingTemplate(models.Model):
    description = models.TextField(blank=True, null=True)
    exercise = models.ManyToManyField(Exercises, related_name='training_temp')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.SET_NULL, null=True, related_name='training_temp')


class Training(models.Model):
    date = models.DateField()
    is_done = models.BooleanField()
    training_template = models.ForeignKey(TrainingTemplate, on_delete=models.CASCADE, related_name='training')
    patient = models.ForeignKey(PatientProfile, on_delete=models.SET_NULL, null=True, related_name='training')


class Progress(models.Model):
    spent_time = models.TimeField()
    count_repeat = models.IntegerField()
    mistakes = models.IntegerField()
    exercise = models.ForeignKey(Exercises, on_delete=models.PROTECT, related_name='progress')
    training = models.ForeignKey(Training, on_delete=models.PROTECT, related_name='progress')
