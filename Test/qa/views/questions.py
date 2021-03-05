from ..models.questions import Question
from ..serializers.questions import QuestionSerializer
from rest_framework_json_api.views import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.core.mail import send_mail
from ..email.config import Config
from rest_framework import status
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)


class QuestionViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            logger.info("Validating data.")
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            logger.info("Data swaved Successfully.")
            headers = self.get_success_headers(serializer.data)
            admin_email = self.get_email(request)
            subject = Config.ANSWER_MESSAGE + ': ' + request.data['Question']
            if request.user.email and admin_email:
                logger.info("Sending Messeage..")
                send_mail(Config.QUESTION_MESSAGE, subject, request.user.email, [admin_email])
                logger.info("Sent Email.")
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            logger.error("Found error while Saving Question data")
            logger.error(e)

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            logger.info("Validating data.")
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            logger.info("Data saved Successfully.")
            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}
            admin_email = self.get_email(request)
            subject = Config.ANSWER_MESSAGE + ': ' + request.data['Question']
            if request.user.email and admin_email:
                logger.info("Sending Messeage..")
                send_mail(Config.QUESTION_MESSAGE, subject, request.user.email, [admin_email])
                logger.info("Sent Email.")
        except Exception as e:
            logger.error("found error While updating the Question data")
            logger.error(e)

    def get_email(self, request):
        user_obj = User.objects.filter(username='admin').first()
        return user_obj.email if user_obj.email else ''
