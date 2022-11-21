from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    salePercent = models.FloatField(default=0)
    in_stock = models.PositiveBigIntegerField(default=0)
    sold = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return str(self.name)


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    is_thumbnail = models.BooleanField()
    url = models.CharField(max_length=200)


class Shoe(models.Model):
    GENDER = [
        (0, "Male"),
        (1, "Female"),
        (2, "Both"),
    ]

    shoe_id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="shoes")
    gender = models.IntegerField(choices=GENDER, default=0)
    series = models.CharField(max_length=100)
    shape = models.BooleanField()


class ShoeChild(models.Model):
    shoe_child_id = models.BigAutoField(primary_key=True)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE, related_name="shoe_childs")
    in_stock = models.PositiveBigIntegerField()
    size = models.PositiveBigIntegerField()


class Accessory(models.Model):
    CATEGORIES = [
        (0, "Shock"),
        (1, "Tote"),
        (2, "Backpack"),
        (3, "Shoelace"),
    ]

    accessory_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="accessories"
    )
    category = models.IntegerField(choices=CATEGORIES, default=0)


class Clothes(models.Model):
    CATEGORIES = [
        (0, "Tee"),
        (1, "Hoodie"),
        (2, "Sweatshirt"),
    ]

    clothes_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="clothes"
    )
    category = models.IntegerField(choices=CATEGORIES, default=0)


class Order(models.Model):
    STATUS = [
        (0, "in progress"),
        (1, "shipping"),
        (2, "done"),
    ]
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    address = models.CharField(max_length=100)
    province_id = models.PositiveBigIntegerField()
    district_id = models.PositiveBigIntegerField()
    commune_id = models.PositiveBigIntegerField()
    status = models.IntegerField(choices=STATUS, default=0)
    total = models.FloatField()
    discount = models.FloatField(default=0)


class OrderProduct(models.Model):
    order_product_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_products"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="order_products"
    )
    price_at_order = models.PositiveBigIntegerField()
    quantity = models.PositiveBigIntegerField()
    size = models.PositiveIntegerField(null=True)


class UserLoveProduct(models.Model):
    user_love_product_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_love_products"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="user_love_products"
    )


class UserCartProduct(models.Model):
    user_cart_product_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_cart_products"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="user_cart_products"
    )
    quantity = models.PositiveBigIntegerField()
    size = models.PositiveIntegerField(null=True)
