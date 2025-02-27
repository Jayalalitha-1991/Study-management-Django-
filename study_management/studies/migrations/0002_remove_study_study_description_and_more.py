# Generated by Django 5.1.2 on 2024-10-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='study',
            name='study_description',
        ),
        migrations.RemoveField(
            model_name='study',
            name='study_name',
        ),
        migrations.RemoveField(
            model_name='study',
            name='study_phase',
        ),
        migrations.AddField(
            model_name='study',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='study',
            name='name',
            field=models.CharField(default='Default Study Name', max_length=100),
        ),
        migrations.AddField(
            model_name='study',
            name='phase',
            field=models.CharField(choices=[('I', 'Phase I'), ('II', 'Phase II'), ('III', 'Phase III'), ('IV', 'Phase IV')], default='I', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='study',
            name='sponsor_name',
            field=models.CharField(default='Unknown Sponsor', max_length=100),
        ),
    ]
