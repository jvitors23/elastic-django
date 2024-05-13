from datetime import datetime, timedelta

from rest_framework.mixins import UpdateModelMixin, CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from elasticsearch import NotFoundError
from django.http import Http404
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.views import extend_schema

from mysite.apps.elastic.models import MySiteDocument
from mysite.apps.elastic.serializers import MySiteDocumentSerializer


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
        timestamp = self.request.GET.get("timestamp", None)

        if timestamp is None:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": "You must provide a timestamp for querying documents."},
            )

        try:
            datetime_object = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
        except Exception:  # noqa: E722
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Invalid timestamp."})

        queryset = self.get_queryset(datetime_object)
        print(queryset)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self, datetime_object):
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
