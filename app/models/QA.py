from peewee import (
  Model,
  IntegerField,
  DateField,
  CharField
)
from db import db

class QAModel(Model):

  user = IntegerField()
  index = IntegerField()
  date = DateField()
  content = CharField()
  reply = CharField(0)

  class Meta:
    database = db

db.create_tables([QAModel])