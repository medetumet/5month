from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from User.serializers import UserValidateSerialiser, UserLoginSerialiser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from User.serializers import UserValidateSerializer, UserCreateSerializer


class AuthorizationCreateAPIView(APIView):

    def post(self, request):
        serializer = UserValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'token': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED,
                        data={'error message': 'User Not Found!'})


@api_view(['POST'])
def authorization_view(request):
    serializer = UserValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'token': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED,
                    data={'error message': 'User Not Found!'})


class RegistrationCreateAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def registration_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    User.objects.create_user(**serializer.validated_data)
    return Response(status=status.HTTP_201_CREATED)