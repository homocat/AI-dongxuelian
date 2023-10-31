from peewee import Model

class BloodModel(Model):
  
  value: int
  increase: int
  decrease: int