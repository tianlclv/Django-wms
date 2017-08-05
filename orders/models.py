from django.db import models


class Order(models.Model):
    ORDER_TYPE_CHOICES = (
        ('ST', '孙老板'),
        ('FW', '微信'),
        ('FT', '淘宝'),
        ('OT', '其他'),
    )
    order_type = models.CharField(
        max_length=10, choices=ORDER_TYPE_CHOICES, default='ST')
    order_money = models.FloatField()
    order_time = models.DateTimeField(auto_now=True)
    ORDER_STATUS_CHOICES = (
        ('JL', '建立订单'),
        ('FH', '订单发货'),
        ('BH', '部分发货'),
        ('CJ', '已成交'),
        ('QX', '订单取消'),
        ('BX', '部分取消'),
    )
    order_status = models.CharField(
        max_length=10, choices=ORDER_STATUS_CHOICES)
    order_eval = models.TextField()
    order_user = models.ForeignKey('Luser')
    order_track = models.ForeignKey('Track')
    order_product = models.ForeignKey('Product')

    def __str__(self):
        return self.order_type


class Address(models.Model):
    
    address_area = models.CharField(
        max_length=10)
    address_province = models.CharField(max_length=20)
    address_city = models.CharField(max_length=50)
    address_class = models.CharField(max_length=50)
    address_full = models.CharField(max_length=100)  

    def __str__(self):
        return self.address_area


class Luser(models.Model):
    user_name = models.CharField(max_length=10)
    user_qq = models.CharField(max_length=15, null=True, blank=True)
    user_weixin = models.CharField(max_length=30, null=True, blank=True)
    user_email = models.EmailField(null=True, blank=True)
    user_phone = models.CharField(max_length=11, null=True, blank=True)
    user_taobao = models.CharField(max_length=30, null=True, blank=True)
    user_weibo = models.CharField(max_length=30, null=True, blank=True)
    user_eval = models.TextField(null=True, blank=True)
    # MangyToManyField中null=True会报fields.W340错误
    user_address = models.ManyToManyField('Address', blank=True)

    def __str__(self):
        return self.user_name


class Track(models.Model):
    TRACK_TYPE_CHOOICES = (
        ('TTO', '天天快递'),
        ('SFO', '顺丰快递'),
        ('ZTO', '中通快递'),
        ('YTO', '圆通快递'),
        ('STO', '申通快递'),
        ('EMS', '邮政EMS'),
        ('YDO', '韵达快递'),
        ('HTO', '汇通快递'),
        ('ZJS', '宅急送'),
        ('BSO', '百世汇通'),
        ('YSO', '优速快递'),
        ('DBO', '德邦物流'),
        ('QTO', '其他'),
    )
    track_type = models.CharField(
        max_length=16, choices=TRACK_TYPE_CHOOICES, default='ZTO')
    track_num = models.CharField(max_length=20)
    track_price = models.FloatField()
    track_printtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.track_type


class Product(models.Model):
    product_type = models.CharField(max_length=20)
    product_cate = models.CharField(max_length=20)
    product_brand = models.CharField(max_length=30)
    product_name = models.CharField(max_length=50)
    product_desc = models.TextField()
    product_price = models.FloatField()

    def __str__(self):
        return self.product_type
