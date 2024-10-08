# Generated by Django 5.0.4 on 2024-05-14 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reauth', '0003_patientprofile'),
        ('retrain', '0003_training'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='training', to='reauth.patientprofile'),
        ),
    ]
