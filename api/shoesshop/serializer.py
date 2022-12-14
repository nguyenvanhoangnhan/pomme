from rest_framework import serializers
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from shoesshop.models import (
    Shoe,
    Product,
    Image,
    Clothes,
    Accessory,
    UserCartProduct,
    UserLoveProduct,
    Order,
    OrderProduct,
    ShoeChild,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_superuser",
        )
        extra_kwargs = {
            "password": {"write_only": True, "required": False},
            "email": {"required": True},
        }

    def create(self, validated_data):
        is_admin = validated_data.get("is_superuser")
        if is_admin:
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)
        return user


class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = "__all__"
        



class ShoeChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeChild
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = "__all__"


class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class UserCartProductSerializer(serializers.ModelSerializer):
    class ProductSerializer(serializers.ModelSerializer):
        images = ImageSerializer(many=True)

        class Meta:
            model = Product
            fields = "__all__"
            extra_kwargs = {
                "images": {"read_only": True, "required": False},
            }

    product = ProductSerializer()

    class Meta:
        model = UserCartProduct
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCartProduct
        fields = "__all__"
       


class UserLoveProductSerializer(serializers.ModelSerializer):
    class ProductSerializer(serializers.ModelSerializer):
        images = ImageSerializer(many=True)

        class Meta:
            model = Product
            fields = "__all__"
            extra_kwargs = {
                "images": {"read_only": True, "required": False},
            }

    product = ProductSerializer()

    class Meta:
        model = UserLoveProduct
        fields = "__all__"


class LoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLoveProduct
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class User_OrderSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        many = True
        model = User
        fields = ("id", "username", "orders")

class Shoe_ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shoe
        fields = ("shoe_id", "gender")



class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'

class OrderedSerializer(serializers.ModelSerializer):
    ProductsOrdered = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ("order_id","user","status","ProductsOrdered","address","province_id","district_id","commune_id","total","discount","order_at","shipping_at","delivered_at")
        depth = 1
    def get_ProductsOrdered(self, obj):

        query_set = OrderProduct.objects.filter(order=obj)

        return [OrderProductSerializer(item).data for item in query_set]   
