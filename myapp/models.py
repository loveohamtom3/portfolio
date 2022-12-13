from django.db import models

class Restaurants(models.Model):
  address = models.TextField('住所')
  description = models.TextField('説明')
  name = models.CharField('店名',max_length=100)
  phone_number = models.CharField('電話番号',max_length=15)
  access = models.TextField('交通アクセス')
  
  def __str__(self):
   return str(self.name)

class Menu(models.Model):
  restaurant_id = models.IntegerField('レストランid')
  name = models.CharField('メニュー名',max_length=100)
  price = models.IntegerField('値段')
  # image = models.ImageField('料理画像',upload_to='media')
  
  def __str__(self):
   return str(self.name)
  
class User(models.Model):
  name = models.CharField('ユーザーネーム',max_length=100)
  
  
  
  
