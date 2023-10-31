from peewee import (
  Model, 
  CharField, 
  IntegerField,
  BooleanField,
  SqliteDatabase
)

db = SqliteDatabase('./test.db')

class Test(Model):
  content = CharField()
  testId = IntegerField()
  testBool = BooleanField()

  class Meta:
    database = db

# 建表
if not db.table_exists('test'):
  db.create_tables([Test])

Test.get(Test.id==1)

# 插入数据
test = Test(content='Hello, World!', testId=1, testBool=True)
test.save()

res = Test.get(testId=1)
print(res)