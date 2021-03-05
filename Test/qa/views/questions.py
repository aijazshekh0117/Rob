from ..models.questions import Question
from ..serializers.questions import QuestionSerializer
from rest_framework_json_api.views import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.core.mail import send_mail
from ..email.config import Config
from rest_framework import status
from rest_framework.response import Response


class QuestionViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        admin_email = self.get_email(request)
        subject = Config.ANSWER_MESSAGE + ': ' + request.data['Question']
        if request.user.email and admin_email:
            send_mail(Config.QUESTION_MESSAGE, subject, request.user.email, [admin_email])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        admin_email = self.get_email(request)
        subject = Config.ANSWER_MESSAGE + ': ' + request.data['Question']
        if request.user.email and admin_email:
            send_mail(Config.QUESTION_MESSAGE, subject, request.user.email, [admin_email])

    def get_email(self, request):
        user_obj = User.objects.filter(username='admin').first()
        return user_obj.email if user_obj.email else ''
