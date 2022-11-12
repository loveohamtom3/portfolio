from django.conf import settings
from django.db import models


class Restaurants(models.Model):
  Address = models.TextField('住所')
  Description = models.TextField('説明')
  Name = models.CharField('名前',max_length=100)
  Menu = models.TextField('メニュー')