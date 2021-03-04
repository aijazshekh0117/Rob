from ..models.questions import Question
from ..serializers.questions import QuestionSerializer
from rest_framework_json_api.views import ModelViewSet


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    class Meta:
        field = '__all__'
