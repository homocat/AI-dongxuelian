from peewee import Model, IntegerField, CharField
from db import db

class MessageModel(Model):
    user = IntegerField()
    index = IntegerField()
    question = CharField()
    ans = CharField()
    voice = CharField()
    date = CharField()

    class Meta:
        database = db

db.create_tables([MessageModel])
