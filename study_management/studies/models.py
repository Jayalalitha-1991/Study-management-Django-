# from django.db import models

# class Study(models.Model):
#     PHASE_CHOICES = [
#         ('Phase I', 'Phase I'),
#         ('Phase II', 'Phase II'),
#         ('Phase III', 'Phase III'),
#         ('Phase IV', 'Phase IV'),
#     ]
#     study_id = models.AutoField(primary_key=True)
#    # name = models.CharField(max_length=100)
#     name = models.CharField(max_length=100, default='Default Study Name')  # Add a suitable default value here
#     description = models.TextField()
#     phase = models.CharField(max_length=10, choices=PHASE_CHOICES)
#     sponsor_name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


from django.db import models

class Study(models.Model):
    PHASE_CHOICES = [
        ('I', 'Phase I'),
        ('II', 'Phase II'),
        ('III', 'Phase III'),
        ('IV', 'Phase IV'),
    ]
    
    study_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='Default Study Name')  # With default value
    description = models.TextField(null=True, blank=True)  # Nullable field
    phase = models.CharField(max_length=10, choices=PHASE_CHOICES)
    sponsor_name = models.CharField(max_length=100, default='Unknown Sponsor')  # With default value
