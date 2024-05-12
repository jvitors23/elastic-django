from django.apps import AppConfig
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

        connections.create_connection(hosts=["http://elasticsearch:9200"], alias="default")
        try:
            MySiteDocument.init()
        except RequestError:
            pass  # The index already exists
