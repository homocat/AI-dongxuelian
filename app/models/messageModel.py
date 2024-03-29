from peewee import (
    IntegerField,
    CharField,
    Model
)
from db import db

class MessageModel(Model):
    user = IntegerField()
    index = IntegerField(0)
    question = CharField()
    ans = CharField()
    voice = CharField()
    date = CharField()

    class Meta:
        database = db

db.create_tables([MessageModel])
