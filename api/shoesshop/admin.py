from django.contrib import admin

from shoesshop.models import (
    Accessory,
    Clothes,
    Image,
    Order,
    OrderProduct,
    Product,
    Shoe,
    ShoeChild,
    UserCartProduct,
    UserLoveProduct,
)

# Register your models here.
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Shoe)
admin.site.register(ShoeChild)
admin.site.register(Accessory)
admin.site.register(Clothes)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(UserLoveProduct)
admin.site.register(UserCartProduct)
