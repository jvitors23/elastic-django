from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from mysite.apps.authentication.serializers import CustomObtainPairSerializer

User = get_user_model()


class CustomObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer


class LogoutView(APIView):
    """Logout view that blacklists jwt token"""

    def post(self, request):
        # Blacklist refresh token
        refresh_token = request.COOKIES.get(settings.SIMPLE_JWT["REFRESH_COOKIE"], "")
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
        return Response(data={"Success": "Logout successfully"})
