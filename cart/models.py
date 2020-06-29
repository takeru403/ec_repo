from django.db import models
#自分でユーザーを設定することができる。
from django.conf import settings
from amazon.models import Product

User = settings.AUTH_USER_MODEL

class Cart(models.Model):
  #一人につき、一つのカートだよという意味の関数
  #nullはデータベースのことで,blankは名前などを書く時に白紙でもいいよという意味
  #on_deleteはForeignKeyでは必須。ユーザーが削除されたら、カートも削除するという意味、。
  user = models.ForeignKey (User, null=True, blank=True ,on_delete=models.CASCADE)
  #これは、カートとユーザーの関係性を作る関数 blankがtrueということは、カートが空でも良いということ
  products = models.ManyToManyField(product, blank=True)
  #decimalは小数点の意味。この場合は９桁の数までお買い物をすることができる。
  total = models.DecimalField(default = 0.00, max_digits=9, decimal_places=2) 
  #カートが作られた時
  created = models.DecimalField(auto_now_add=True)
  #カートが更新されるごと
  updated=models.DateTimeField(auto_now=True)
# Create your models here.
