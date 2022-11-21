from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
<<<<<<< HEAD
    salePercent = models.FloatField(default=0)
    in_stock = models.PositiveBigIntegerField(default=0)
    sold = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return str(self.name)
=======
    salePercent = models.FloatField()
    in_stock = models.PositiveBigIntegerField()
    sold = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.name
>>>>>>> develop


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
<<<<<<< HEAD
        Product, on_delete=models.CASCADE, related_name="images"
    )
    is_thumbnail = models.BooleanField()
    url = models.CharField(max_length=200)
=======
        Product, on_delete=models.CASCADE, related_name='images')
    is_thumbnail = models.BooleanField()
    url = models.URLField()
>>>>>>> develop


class Shoe(models.Model):
    GENDER = [
<<<<<<< HEAD
        (0, "Male"),
        (1, "Female"),
        (2, "Both"),
    ]

    shoe_id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="shoes")
=======
        (0, 'Male'),
        (1, 'Female'),
        (2, 'Both'),
    ]

    shoe_id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='shoes')
>>>>>>> develop
    gender = models.IntegerField(choices=GENDER, default=0)
    series = models.CharField(max_length=100)
    shape = models.BooleanField()


class ShoeChild(models.Model):
    shoe_child_id = models.BigAutoField(primary_key=True)
<<<<<<< HEAD
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE, related_name="shoe_childs")
=======
    shoe = models.ForeignKey(
        Shoe, on_delete=models.CASCADE, related_name='shoe_childs')
>>>>>>> develop
    in_stock = models.PositiveBigIntegerField()
    size = models.PositiveBigIntegerField()


class Accessory(models.Model):
    CATEGORIES = [
<<<<<<< HEAD
        (0, "Shock"),
        (1, "Tote"),
        (2, "Backpack"),
        (3, "Shoelace"),
=======
        (0, 'Shock'),
        (1, 'Tote'),
        (2, 'Backpack'),
        (3, 'Shoelace'),
>>>>>>> develop
    ]

    accessory_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
<<<<<<< HEAD
        Product, on_delete=models.CASCADE, related_name="accessories"
    )
=======
        Product, on_delete=models.CASCADE, related_name='accessories')
>>>>>>> develop
    category = models.IntegerField(choices=CATEGORIES, default=0)


class Clothes(models.Model):
    CATEGORIES = [
<<<<<<< HEAD
        (0, "Tee"),
        (1, "Hoodie"),
        (2, "Sweatshirt"),
=======
        (0, 'Tee'),
        (1, 'Hoodie'),
        (2, 'Sweatshirt'),
>>>>>>> develop
    ]

    clothes_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
<<<<<<< HEAD
        Product, on_delete=models.CASCADE, related_name="clothes"
    )
=======
        Product, on_delete=models.CASCADE, related_name='clothes')
>>>>>>> develop
    category = models.IntegerField(choices=CATEGORIES, default=0)


class Order(models.Model):
    STATUS = [
<<<<<<< HEAD
        (0, "in progress"),
        (1, "shipping"),
        (2, "done"),
    ]
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
=======
        (0, 'in progress'),
        (1, 'shipping'),
        (2, 'done'),
    ]
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders')
>>>>>>> develop
    address = models.CharField(max_length=100)
    province_id = models.PositiveBigIntegerField()
    district_id = models.PositiveBigIntegerField()
    commune_id = models.PositiveBigIntegerField()
    status = models.IntegerField(choices=STATUS, default=0)
<<<<<<< HEAD
    total = models.FloatField()
    discount = models.FloatField(default=0)
=======
>>>>>>> develop


class OrderProduct(models.Model):
    order_product_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(
<<<<<<< HEAD
        Order, on_delete=models.CASCADE, related_name="order_products"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="order_products"
    )
=======
        Order, on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='order_products')
>>>>>>> develop
    price_at_order = models.PositiveBigIntegerField()
    quantity = models.PositiveBigIntegerField()
    size = models.PositiveIntegerField(null=True)



class UserLoveProduct(models.Model):
    user_love_product_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
<<<<<<< HEAD
        User, on_delete=models.CASCADE, related_name="user_love_products"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="user_love_products"
    )
=======
        User, on_delete=models.CASCADE, related_name='user_love_products')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='user_love_products')
>>>>>>> develop


class UserCartProduct(models.Model):
    user_cart_product_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
<<<<<<< HEAD
        User, on_delete=models.CASCADE, related_name="user_cart_products"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="user_cart_products"
    )
    quantity = models.PositiveBigIntegerField()
    size = models.PositiveIntegerField(null=True)
=======
        User, on_delete=models.CASCADE, related_name='user_cart_products')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='user_cart_products')
>>>>>>> develop
