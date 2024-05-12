from django.urls import path

from mysite.apps.users import views

urlpatterns = [
    path("me/", views.ManageUserView.as_view(), name="manage_user"),
]
