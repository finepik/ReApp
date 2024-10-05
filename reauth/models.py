from django.contrib.auth.models import User
from django.db import models


class DoctorProfile(models.Model):
    education = models.CharField(max_length=127, blank=True, null=True)
    experience_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="photos/doctor-profile/", blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')


class Diagnosis(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=127)
    description = models.TextField( blank=True, null=True)


class PatientProfile(models.Model):
    birth_date = models.DateField(blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    attachment_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to="photos/patient-profile/", blank=True, null=True)
    characteristics = models.CharField(max_length=255, blank=True, null=True)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.SET_NULL, null=True, related_name='patients')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.PROTECT, related_name='patients')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
