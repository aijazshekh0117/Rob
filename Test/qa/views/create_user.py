from django.contrib.auth.models import User
from ..serializers import UserSerializer
from rest_framework.response import Response
from rest_framework_json_api.views import ModelViewSet
from  rest_framework import status


class CreateUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self):

        serialized = UserSerializer(data=self.request.data)
        if serialized.is_valid():
            User.objects.create_user(
                serialized.init_data['email'],
                serialized.init_data['username'],
                serialized.init_data['password']
            )
            return Response(self.serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(self.serialized._errors, status=status.HTTP_400_BAD_REQUEST)