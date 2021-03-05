from django.contrib.auth.models import User
from ..serializers import UserSerializer
from rest_framework.response import Response
from rest_framework_json_api.views import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework_jwt.serializers import jwt_payload_handler
import jwt
from rest_framework.permissions import AllowAny
from django.conf import settings

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


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    try:
        email = request.data['email']
        password = request.data['password']

        user = User.objects.get(email=email, password=password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['name'] = "%s %s" % (
                    user.first_name, user.last_name)
                user_details['token'] = token
                # user_logged_in.send(sender=user.__class__,
                #                     request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)

            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide a email and a password'}
        return Response(res)