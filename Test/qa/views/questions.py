from ..models.questions import Question
from ..serializers.questions import QuestionSerializer
from rest_framework_json_api.views import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class QuestionViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    class Meta:
        field = '__all__'
