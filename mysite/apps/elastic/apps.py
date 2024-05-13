from django.apps import AppConfig
from django.conf import settings
from elasticsearch import ElasticsearchWarning
from elasticsearch.exceptions import RequestError
from elasticsearch_dsl.connections import connections
import logging
import warnings


warnings.simplefilter("ignore", category=ElasticsearchWarning)
logging.getLogger("elasticsearch").setLevel(logging.ERROR)


class ElasticConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mysite.apps.elastic"

    def ready(self):
        from .models import MySiteDocument

        connections.create_connection(hosts=[f"http://{settings.ES_HOSTNAME}:{settings.ES_PORT}"], alias="default")
        try:
            MySiteDocument.init(index=settings.ES_INDEX_NAME)
        except RequestError:
            pass  # The index already exists
