from django.urls import path

from mysite.apps.users import views

urlpatterns = [
    path("register/", views.CreateUserView.as_view(), name="register_user"),
    path("me/", views.ManageUserView.as_view(), name="manage_user"),
]
