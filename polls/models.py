from django.db import models
from django.db.models.signals import post_save, pre_save
# Create your models here.
from django.dispatch import receiver
from django.contrib.auth.models import User


class UserProfileManager(models.Manager):
  def get_queryset(self):
    return super(UserProfileManager, self).get_queryset().filter(city='London')


# ˇ如何在配置文件頁面上的模板中顯示用戶配置文件模型信息（Django 教程） | 第 35 部分 ***它的信號根本沒有用
class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
  description = models.CharField(max_length=100, default='')
  city = models.CharField(max_length=100, default='')
  website = models.URLField(default='')
  phone = models.IntegerField(default=0)
  image = models.ImageField(upload_to='profile_image', blank=True)

  london = UserProfileManager()

  def __str__(self):
    return self.user.username


class Store(models.Model):  # 商店
  store_name = models.CharField(max_length=10)  # 店家的名稱
  store_holder = models.CharField(max_length=50)  # 店家持有人名字
  store_phoneNumber = models.CharField(max_length=10)  # 店家的電話號碼
  store_address = models.CharField(max_length=100)  # 店家的地址
  store_email = models.EmailField(max_length=60,
                                  default='',
                                  help_text='必需的。 添加有效的電子郵件地址', verbose_name='郵件信箱',
                                  unique=True, )
  store_notes = models.TextField(blank=True, default='')  # 店家的筆記

  def __str__(self):
    return self.store_name


def create_store_profile(sender, **kwargs):
  if kwargs['created']:
    store_profile = Store.objects.create(user=kwargs['instance'])


post_save.connect(create_store_profile, sender=Store)

SIZE_CHOICES = [
  ('BG', 'Big'),
  ('MD', 'Middle'),
  ('SM', 'Small'),
]


class MenuItem(models.Model):  # 菜單
  menuItem_name = models.CharField(max_length=50)  # 菜單名稱
  menuItem_price = models.DecimalField(max_digits=3, decimal_places=0)  # 菜單名稱價位
  menuItem_meals_size = models.CharField(max_length=9, choices=SIZE_CHOICES, default='Big')  # 項目餐點大小
  menuItem_store = models.ForeignKey('Store', related_name='menu_items', on_delete=models.CASCADE)  # 店家名字
  menuItem_notes = models.TextField(blank=True, default='')  # 菜單的筆記

  def __str__(self):
    return self.menuItem_name


class Vendor(models.Model):
  vendor_store_name = models.CharField(max_length=20)  # 攤販的名稱
  vendor_holder_name = models.CharField(max_length=10)  # 攤販店家持有人
  vendor_phone_number = models.CharField(max_length=20)  # 攤販的電話號碼
  vendor_address = models.CharField(max_length=100)  # 攤販的地址
  vendor_notes = models.TextField(blank=True, default='')  # 攤販的筆記

  def __str__(self):
    return self.vendor_store_name


UNIT_CHOICES = [
  ('公克', 'Gram'),
  ('公斤', 'Kilogram'),
  ('台斤', 'catty'),
  ('毫克', 'Milligrams'),
]


class Ingredients(models.Model):
  ingredients_name = models.CharField(max_length=30)  # 食物名稱
  ingredients_price = models.DecimalField(max_digits=3, decimal_places=0)  # 食物價錢
  ingredients_unit = models.CharField(max_length=9, choices=UNIT_CHOICES, default='公克g')  # 食物價錢
  ingredients_vendor = models.ForeignKey(Vendor, related_name='ingredients_menu_items',
                                         on_delete=models.CASCADE)  # 代表這食物是由哪一個攤販所做的
  ingredients_notes = models.TextField(blank=True, default='')  # 食材的筆記

  def __str__(self):
    return self.ingredients_name
