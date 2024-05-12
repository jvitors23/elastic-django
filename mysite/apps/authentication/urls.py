from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from mysite.apps.authentication import views

urlpatterns = [
    path("token/", views.CustomObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
