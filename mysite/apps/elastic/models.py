from django.conf import settings
from datetime import datetime
from elasticsearch_dsl import Document, Date, Keyword, Float, Nested, InnerDoc


class User(InnerDoc):
    id = Keyword()
    training = Float()


class MySiteDocument(Document):
    id = Keyword()
    user = Nested(User)
    request_id = Keyword()
    alerts = Keyword(multi=True)
    IP = Keyword()
    user_agent = Keyword()
    timestamp = Date()

    class Index:
        name = settings.ES_INDEX_NAME
        settings = {
            "number_of_shards": 2,
        }

    def save(self, **kwargs):
        self.timestamp = datetime.now()
        return super(MySiteDocument, self).save(**kwargs)
