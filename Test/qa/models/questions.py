from django.db import models
from django.core.mail import send_mail


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=1000)
