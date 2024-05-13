from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(prefix="documents", viewset=views.MySiteDocumentViewSet, basename="documents")

app_name = "elastic"

urlpatterns = [
    path("", include(router.urls)),
]
