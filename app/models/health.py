from db import db
from peewee import (
  Model,
  FloatField,
  ForeignKeyField
)
from .user import UserModel

class HealthModel(Model):
  user = ForeignKeyField(UserModel)
  bloodpresure = FloatField()
  heartrate = FloatField()

  class Meta:
    database = db
