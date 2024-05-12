from django.contrib.auth import password_validation
from rest_framework import serializers

from mysite.apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user objects"""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        )
        read_only_fields = ("id", "username")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def update(self, instance: User, validated_data: dict) -> User:
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
