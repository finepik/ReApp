from django.contrib import admin

from .models import DoctorProfile, PatientProfile, Diagnosis

admin.site.register(DoctorProfile)
admin.site.register(PatientProfile)
admin.site.register(Diagnosis)
