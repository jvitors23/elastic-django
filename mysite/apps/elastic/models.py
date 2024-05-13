from django.conf import settings
from elasticsearch_dsl import Document, Date, Keyword, Float, Nested, InnerDoc


class User(InnerDoc):
    id = Keyword()
    training = Float()


class MySiteDocument(Document):
    id = Keyword()
    user = Nested(User)
    request_id = Keyword()
    alerts = Keyword(multi=True)
    ip_address = Keyword()
    user_agent = Keyword()
    timestamp = Date()

    class Index:
        name = settings.ES_INDEX_NAME
        settings = {
            "number_of_shards": 2,
        }
