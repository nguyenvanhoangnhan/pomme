from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, JSONParser
import cloudinary.uploader
from rest_framework import status, viewsets
from django.contrib.auth.models import User
from .imageView import ImageView
from .productView import ProductView
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


class AccessoryView(viewsets.ViewSet):
    serializer_class = AccessorySerializer
    queryset = Accessory.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            product = ProductView.createProduct(request.data["product"], 3)
            for img in request.data["image"]:
                image = {
                    "product": product,
                    "url": img["url"],
                    "is_thumbnail": img["is_thumbnail"],
                }
                ImageView.createImage(image)
            data = {
                "product": product,
                "category": request.data["accessory"]["category"],
            }
            serializer = AccessorySerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "message": "Accessory Created Successfully!",
                },
                status=status.HTTP_201_CREATED,
            )
        except:
            return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            accessory = Accessory.objects.get(pk=pk)
            images = ImageView.getListImage(accessory.product.product_id)
            product = {
                "product_id": accessory.product.product_id,
                "name": accessory.product.name,
                "price": accessory.product.price,
                "salePercent": accessory.product.salePercent,
                "in_stock": accessory.product.in_stock,
                "sold": accessory.product.sold,
                "image": images,
            }
            data = {
                "accessory_id": accessory.accessory_id,
                "category": accessory.category,
                "product": product,
            }
            # serializer = ShoeSerializer(instance=shoe)
            return Response(
                {
                    "data": data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Accessory not found!",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    @api_view(["GET"])
    def getListAccessory(self, page=None):
        try:
            page = page
            fistItem = (page - 1) * 12
            data = []
            accessories = Accessory.objects.all()[
                fistItem : fistItem + 12
            ].select_related("product")
            for a in accessories:
                images = ImageView.getListImage(a.product.product_id)
                product = {
                    "product_id": a.product.product_id,
                    "name": a.product.name,
                    "price": a.product.price,
                    "salePercent": a.product.salePercent,
                    "in_stock": a.product.in_stock,
                    "sold": a.product.sold,
                    "image": images,
                }
                data.append(
                    {
                        "accessory_id": a.accessory_id,
                        "category": a.category,
                        "product": product,
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
                {
                    "message": "error",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    # filter by sale, category, price
    @api_view(["GET"])
    def filterAccessory(request, page=None, sale=None, category=None, price=None):
        try:
            page, sale, category, price = page, sale, category, price
            fistItem = (page - 1) * 12
            data = []
            accessories = []
            # sale
            if sale == 1:
                # have cate
                if category != 0:
                    if price == 1:
                        accessories = Accessory.objects.filter(
                            product__salePercent__gt=0, category=category
                        ).order_by("product__price")[fistItem : fistItem + 12]
                    if price == 2:
                        accessories = Accessory.objects.filter(
                            product__salePercent__gt=0, category=category
                        ).order_by("-product__price")[fistItem : fistItem + 12]
                    if price == 0:
                        accessories = Accessory.objects.filter(
                            product__salePercent__gt=0, category=category
                        )[fistItem : fistItem + 12]
                # not have cate
                else:
                    if price == 1:
                        accessories = Accessory.objects.filter(
                            product__salePercent__gt=0
                        ).order_by("product__price")[fistItem : fistItem + 12]
                    if price == 2:
                        accessories = Accessory.objects.filter(
                            product__salePercent__gt=0
                        ).order_by("-product__price")[fistItem : fistItem + 12]
                    if price == 0:
                        accessories = Accessory.objects.filter(
                            product__salePercent__gt=0
                        )[fistItem : fistItem + 12]
            # not sale
            else:
                # have cate
                if category != 0:
                    if price == 1:
                        accessories = Accessory.objects.filter(
                            category=category
                        ).order_by("product__price")[fistItem : fistItem + 12]
                    if price == 2:
                        accessories = Accessory.objects.filter(
                            category=category
                        ).order_by("-product__price")[fistItem : fistItem + 12]
                    if price == 0:
                        accessories = Accessory.objects.filter(category=category)[
                            fistItem : fistItem + 12
                        ]
                # not have cate
                else:
                    if price == 1:
                        accessories = Accessory.objects.all().order_by(
                            "product__price"
                        )[fistItem : fistItem + 12]
                    if price == 2:
                        accessories = Accessory.objects.all().order_by(
                            "-product__price"
                        )[fistItem : fistItem + 12]
            for a in accessories:
                images = ImageView.getListImage(a.product.product_id)
                product = {
                    "product_id": a.product.product_id,
                    "name": a.product.name,
                    "price": a.product.price,
                    "salePercent": a.product.salePercent,
                    "in_stock": a.product.in_stock,
                    "sold": a.product.sold,
                    "image": images,
                }
                data.append(
                    {
                        "clothes_id": a.clothes_id,
                        "category": a.category,
                        "product": product,
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
