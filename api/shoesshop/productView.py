from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, JSONParser
import cloudinary.uploader
from rest_framework import status, viewsets
from django.contrib.auth.models import User
from .imageView import ImageView
from shoesshop.models import (
    Shoe,
    Product,
    Image,
    Clothes,
    Accessory,
    UserCartProduct,
    UserLoveProduct,
)
from shoesshop.serializer import (
    CartSerializer,
    LoveSerializer,
    ShoeSerializer,
    UserSerializer,
    ProductSerializer,
    ImageSerializer,
    UserCartProductSerializer,
    UserLoveProductSerializer,
    AccessorySerializer,
    ClothesSerializer,
    User_OrderSerializer,
)


class ProductView(viewsets.ViewSet):
    def createProduct(data, type):
        data = {"name": data["name"], "price": data["price"], "type": type}
        serializer = ProductSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        return serializer["product_id"].value

    @api_view(["DELETE"])
    def deleteProduct(request, id=None):
        # delete an object and send a confirmation response
        try:
            Product.objects.get(product_id=id).delete()
            return Response(
                {
                    "message": "Product delete Successfully!",
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Product not found!",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    @api_view(["GET"])
    def getProductByID(request, id=None):
        try:
            id = id
            product = Product.objects.get(product_id=id)
            images = ImageView.getListImage(product.product_id)
            product = {
                "product_id": product.product_id,
                "name": product.name,
                "price": product.price,
                "salePercent": product.salePercent,
                "in_stock": product.in_stock,
                "sold": product.sold,
                "type": product.type,
                "image": images,
            }
            # serializer = ShoeSerializer(instance=shoe)
            return Response(
                {
                    "data": product,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Product not found!",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    @api_view(["GET"])
    def getDetailTypeByID(request, id=None):
        try:
            id = id
            data = {}
            product = Product.objects.get(product_id=id)
            images = ImageView.getListImage(id)
            productDT = {
                "product_id": product.product_id,
                "name": product.name,
                "price": product.price,
                "salePercent": product.salePercent,
                "in_stock": product.in_stock,
                "sold": product.sold,
                "type": product.type,
                "images": images,
            }
            if product.type == 1:
                shoe = Shoe.objects.filter(product_id=id)[0]
                data = {
                    "shoe_id": shoe.shoe_id,
                    "gender": shoe.gender,
                    "shape": shoe.shape,
                    "series": shoe.series,
                    "product": productDT,
                }
            if product.type == 2:
                accessory = Accessory.objects.filter(product_id=id)[0]
                print(accessory)
                data = {
                    "accessory_id": accessory.accessory_id,
                    "category": accessory.category,
                    "product": productDT,
                }
            if product.type == 3:
                cloth = Clothes.objects.filter(product_id=id)[0]
                data = {
                    "clothes_id": cloth.clothes_id,
                    "category": cloth.category,
                    "product": productDT,
                }

            return Response(
                {
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Product not found!",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    @api_view(["GET"])
    def getListProduct(self, page=None):
        try:
            page = page
            fistItem = (page - 1) * 12
            data = []
            products = Product.objects.all()[fistItem: fistItem + 12]
            for product in products:
                images = ImageView.getListImage(product.product_id)
                data.append(
                    {
                        "product_id": product.product_id,
                        "name": product.name,
                        "price": product.price,
                        "salePercent": product.salePercent,
                        "in_stock": product.in_stock,
                        "sold": product.sold,
                        "type": product.type,
                        "images": images,
                    }
                )
            return Response(
                {
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {"message": "error"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @api_view(["GET"])
    def searchProduct(self, page=None, key=None):
        try:
            page = page
            key = key
            fistItem = (page - 1) * 12
            data = []
            products = Product.objects.filter(name__contains=key)[
                fistItem: fistItem + 12
            ]
            for product in products:
                images = ImageView.getListImage(product.product_id)
                data.append(
                    {
                        "product_id": product.product_id,
                        "name": product.name,
                        "price": product.price,
                        "salePercent": product.salePercent,
                        "in_stock": product.in_stock,
                        "sold": product.sold,
                        "type": product.type,
                        "images": images,
                    }
                )
            return Response(
                {
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {"message": "error"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    # filter by sale and price
    @api_view(["GET"])
    def filterProduct(request, page=None, sale=None, price=None):
        try:
            page, sale, price = page, sale, price
            fistItem = (page - 1) * 12
            data = []
            products = []
            # sale and asc price
            if sale == 1 and price == 1:
                products = Product.objects.filter(salePercent__gt=0).order_by("price")[
                    fistItem: fistItem + 12
                ]
            # sale and dsc price
            if sale == 1 and price == 2:
                products = Product.objects.filter(salePercent__gt=0).order_by("-price")[
                    fistItem: fistItem + 12
                ]
            # sale and not sort by price
            if sale == 1 and price == 0:
                products = Product.objects.filter(salePercent__gt=0)[
                    fistItem: fistItem + 12
                ]
            # not sale and asc price
            if sale == 0 and price == 1:
                products = Product.objects.order_by(
                    "price")[fistItem: fistItem + 12]
            # not sale and dsc price
            if sale == 0 and price == 2:
                products = Product.objects.order_by(
                    "-price")[fistItem: fistItem + 12]
            for product in products:
                images = ImageView.getListImage(product.product_id)
                data.append(
                    {
                        "product_id": product.product_id,
                        "name": product.name,
                        "price": product.price,
                        "salePercent": product.salePercent,
                        "in_stock": product.in_stock,
                        "sold": product.sold,
                        "type": product.type,
                        "images": images,
                    }
                )
            return Response(
                {
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {"message": "error"},
                status=status.HTTP_400_BAD_REQUEST,
            )
