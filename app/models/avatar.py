from peewee import (
    Model,
    IntegerField,
    BlobField
)
from db import db

class BaseModel(Model):
    class Meta:
        database = db

class AvatarModel(BaseModel):
    user_id = IntegerField(unique=True)
    file_data = BlobField(null=True)

db.create_tables([AvatarModel])