from peewee import (
  Model,
  CharField,
  BooleanField,
  SqliteDatabase
)
db = SqliteDatabase('./test.db')

class UserModel(Model):
  username = CharField()
  password = CharField()
  email = CharField()
  disabled = BooleanField(default=False)

  class Meta:
    database = db

db.create_tables([UserModel])


test = UserModel(username='admin', password='admin', email="adf")
test = UserModel(username='a', password='admin', email="adf")
test.save()
res = UserModel.get(UserModel.username=='a')


print(res)