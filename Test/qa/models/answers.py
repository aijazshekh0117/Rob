from django.db import models
from .questions import Question


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Answer = models.CharField(max_length=100000)
    file = models.FileField(null=True, blank=True)

