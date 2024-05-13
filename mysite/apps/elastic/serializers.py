from rest_framework import serializers
from mysite.apps.elastic.models import MySiteDocument, User
from django.utils import timezone


class UserDataSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    training = serializers.FloatField()

    class Meta:
        read_only_fields = ("id",)
        extra_kwargs = {"password": {"write_only": True}}


class MySiteDocumentSerializer(serializers.Serializer):
    """Serializer for the MySiteDocument objects"""

    id = serializers.UUIDField()
    timestamp = serializers.DateTimeField()
    user = UserDataSerializer()
    alerts = serializers.ListField(child=serializers.CharField())
    request_id = serializers.CharField()
    ip_address = serializers.IPAddressField()
    user_agent = serializers.CharField()

    def save(self):
        return MySiteDocument(
            meta={"id": self.validated_data["id"]},
            id=self.validated_data["id"],
            user=User(
                id=self.validated_data["user"]["id"],
                training=self.validated_data["user"]["training"],
            ),
            request_id=self.validated_data["request_id"],
            alerts=self.validated_data["alerts"],
            ip_address=self.validated_data["ip_address"],
            user_agent=self.validated_data["user_agent"],
            timestamp=timezone.now(),
        ).save()

    class Meta:
        read_only_fields = ("id", "timestamp")
        extra_kwargs = {"password": {"write_only": True}}
