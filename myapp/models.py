from time import timezone
from django.db import models
from django.contrib.auth.models import User


class Restaurants(models.Model):
  address = models.TextField('住所')
  description = models.TextField('説明')
  name = models.CharField('店名',max_length=100)
  phoneNumber = models.CharField('電話番号',max_length=15)
  access = models.TextField('交通アクセス')
  category = models.TextField('カテゴリー')
  place = models.TextField('地域')
  lunchPrice = models.IntegerField('ランチ料金')
  dinnerPrice = models.IntegerField('ディナー料金')
  map = models.URLField('地図',max_length=1000)
  photo = models.URLField('画像')
  
  def menus(self):
   return Menu.objects.filter(restaurant_id=self.id)

  def __str__(self):
   return str(self.name)

class Menu(models.Model):
  restaurant_id = models.ForeignKey(Restaurants,verbose_name="レストラン",on_delete=models.CASCADE)
  name = models.CharField('メニュー名',max_length=100)
  price = models.IntegerField('値段')
  photo = models.URLField('画像')

  
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
        unique_together = ('restaurant_id', 'user','restaurant_name')

    def __str__(self):
        return str(self.restaurant_id)

    def get_percent(self):
        percent = round(self.score / 5 * 100)
        return percent
class Like(models.Model):
    """お気に入り"""
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Consideration(models.Model):
    """検討リスト"""
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


