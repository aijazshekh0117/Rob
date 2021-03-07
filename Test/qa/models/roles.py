from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    CHOICES = (
        ('Mentor', 'MENTOR'),
        ('User', 'USER'),

    )
    role = models.CharField(choices=CHOICES, max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)