from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from User.serializers import UserValidateSerialiser, UserLoginSerialiser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def registration_view(request):
    serializer = UserValidateSerialiser(data=request.data)
    serializer.is_valid(raise_exception=True)
    User.objects.create_user(username=serializer.validated_data.get('username'),
                             password=serializer.validated_data.get('password'))
    # User.objects.create_user(**serializer.validated_data)
    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def authorization_view(request):
    serializer = UserLoginSerialiser(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(username=serializer.validated_data.get('username'),
                        password=serializer.validated_data.get('password'))
    # user = authenticate(**serializer.validated_data)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response(status=status.HTTP_401_UNAUTHORIZED)