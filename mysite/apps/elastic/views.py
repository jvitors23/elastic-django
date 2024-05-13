from datetime import datetime, timedelta

from rest_framework.mixins import UpdateModelMixin, CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from elasticsearch import NotFoundError
from django.http import Http404
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.views import extend_schema

from mysite.apps.elastic.models import MySiteDocument
from mysite.apps.elastic.serializers import MySiteDocumentSerializer, ListDocumentsSerializer


class MySiteDocumentViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet,
):
    serializer_class = MySiteDocumentSerializer
    lookup_field = "id"

    def get_object(self) -> MySiteDocument:
        try:
            return MySiteDocument.get(id=self.kwargs["id"])
        except NotFoundError:
            raise Http404()

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="timestamp", description="Timestamp used to filter documents.", required=True, type=str
            ),
        ],
        description="More descriptive text",
    )
    def list(self, request, *args, **kwargs):
        serializer = ListDocumentsSerializer(data=self.request.GET)
        serializer.is_valid(raise_exception=True)
        timestamp = serializer.validated_data["timestamp"]
        queryset = self.get_queryset(timestamp)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self, datetime_object: datetime):
        return (
            MySiteDocument.search()
            .filter(
                "range",
                timestamp={
                    "gte": datetime_object - timedelta(hours=1),
                    "lte": datetime_object + timedelta(hours=1),
                },
            )
            .execute()
        )
