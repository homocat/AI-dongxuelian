from peewee import (
  Model, 
  CharField, 
  IntegerField,
  BooleanField
)

from app.db.connection import db

class Test(Model):
  content = CharField()
  testId = IntegerField()
  testBool = BooleanField()

  class Meta:
    database = db

# 建表
if not db.table_exists('test'):
  db.create_tables([Test])

# 插入数据
test = Test(content='Hello, World!', testId=1, testBool=True)
test.save()