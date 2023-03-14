from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserLoginSerialiser(serializers.Serializer):
    username = serializers.Charfield()
    password = serializers.Charfield()
class UserValidateSerialiser(UserLoginSerialiser):
    username = serializers.Charfield()
    password = serializers.Charfield()

    def validate_username(self, username):
        try:
            User.Objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists!')
