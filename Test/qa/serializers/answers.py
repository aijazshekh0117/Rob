from rest_framework import serializers
from ..models.answers import Answer


class AnswerSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Answer
        fields = '__all__'
