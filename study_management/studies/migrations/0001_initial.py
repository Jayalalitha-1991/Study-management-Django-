# Generated by Django 5.1.2 on 2024-10-15 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('study_id', models.AutoField(primary_key=True, serialize=False)),
                ('study_name', models.CharField(max_length=255)),
                ('study_description', models.TextField()),
                ('study_phase', models.CharField(choices=[('Phase I', 'Phase I'), ('Phase II', 'Phase II'), ('Phase III', 'Phase III'), ('Phase IV', 'Phase IV')], max_length=20)),
                ('sponsor_name', models.CharField(max_length=255)),
            ],
        ),
    ]
