from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser


class Restaurants(models.Model):
  address = models.TextField('住所')
  description = models.TextField('説明')
  name = models.CharField('店名',max_length=100)
  phone_number = models.CharField('電話番号',max_length=15)
  access = models.TextField('交通アクセス')
  category = models.TextField('カテゴリー')
  place = models.TextField('地域')
  lunchPrice = models.TextField('ランチ料金')
  dinnerPrice = models.TextField('ディナー料金')
  
  def __str__(self):
   return str(self.name)

class Menu(models.Model):
  restaurant_id = models.IntegerField('レストランid')
  name = models.CharField('メニュー名',max_length=100)
  price = models.IntegerField('値段')
  # image = models.ImageField('料理画像',upload_to='media')
  
  def __str__(self):
   return str(self.name)
 
SCORE_CHOICES = [
    (1, '★'),
    (2, '★★'),
    (3, '★★★'),
    (4, '★★★★'),
    (5, '★★★★★'),
]

class Review(models.Model):
    restaurant_id = models.CharField('レストランID', max_length=10, blank=False)
    restaurant_name = models.CharField('店名', max_length=200, blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.TextField(verbose_name='レビューコメント', blank=False)
    score = models.PositiveSmallIntegerField(verbose_name='レビュースコア', choices=SCORE_CHOICES, default='3')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('restaurant_id', 'user')

    def __str__(self):
        return str(self.restaurant_id)

    def get_percent(self):
        percent = round(self.score / 5 * 100)
        return percent

  
  
  
  
