from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "username"

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["email"] = user.email
        token["first_name"] = user.first_name
        return token
