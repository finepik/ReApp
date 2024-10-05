from django.contrib import admin

from .models import Exercises, TrainingTemplate, Training, Progress

admin.site.register(Exercises)
admin.site.register(TrainingTemplate)
admin.site.register(Training)
admin.site.register(Progress)