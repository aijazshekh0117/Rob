from ..models.answers import Answer
from ..serializers.answers import AnswerSerializer
from rest_framework_json_api.views import ModelViewSet


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    class Meta:
        field = '__all__'
