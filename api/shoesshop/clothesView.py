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


class ClothesView(viewsets.ViewSet):
    serializer_class = ClothesSerializer
    queryset = Clothes.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            product = ProductView.createProduct(request.data["product"], 2)
            for img in request.data["image"]:
                image = {
                    "product": product,
                    "url": img["url"],
                    "is_thumbnail": img["is_thumbnail"],
                }
                ImageView.createImage(image)
            data = {
                "product": product,
                "category": request.data["cloth"]["category"],
            }
            serializer = ClothesSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "message": "Cloth Created Successfully!",
                },
                status=status.HTTP_201_CREATED,
            )
        except:
            return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            cloth = Clothes.objects.get(pk=pk)
            images = ImageView.getListImage(cloth.product.product_id)
            product = {
                "product_id": cloth.product.product_id,
                "name": cloth.product.name,
                "price": cloth.product.price,
                "salePercent": cloth.product.salePercent,
                "in_stock": cloth.product.in_stock,
                "sold": cloth.product.sold,
                "image": images,
            }
            data = {
                "clothes_id": cloth.clothes_id,
                "category": cloth.category,
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
                    "message": "Cloth not found!",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    @api_view(["GET"])
    def getListClothes(self, page=None):
        try:
            page = page
            fistItem = (page - 1) * 12
            data = []
            clothes = Clothes.objects.all()[fistItem : fistItem + 12].select_related(
                "product"
            )
            for c in clothes:
                images = ImageView.getListImage(c.product.product_id)
                product = {
                    "product_id": c.product.product_id,
                    "name": c.product.name,
                    "price": c.product.price,
                    "salePercent": c.product.salePercent,
                    "in_stock": c.product.in_stock,
                    "sold": c.product.sold,
                    "image": images,
                }
                data.append(
                    {
                        "clothes_id": c.clothes_id,
                        "category": c.category,
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
    def filterClothes(request, page=None, sale=None, category=None, price=None):
        try:
            page, sale, category, price = page, sale, category, price
            fistItem = (page - 1) * 12
            data = []
            clothes = []
            # sale
            if sale == 1:
                # have cate
                if category != 0:
                    if price == 1:
                        clothes = Clothes.objects.filter(
                            product__salePercent__gt=0, category=category
                        ).order_by("product__price")[fistItem : fistItem + 12]
                    if price == 2:
                        clothes = Clothes.objects.filter(
                            product__salePercent__gt=0, category=category
                        ).order_by("-product__price")[fistItem : fistItem + 12]
                    if price == 0:
                        clothes = Clothes.objects.filter(
                            product__salePercent__gt=0, category=category
                        )[fistItem : fistItem + 12]
                # not have cate
                else:
                    if price == 1:
                        clothes = Clothes.objects.filter(
                            product__salePercent__gt=0
                        ).order_by("product__price")[fistItem : fistItem + 12]
                    if price == 2:
                        clothes = Clothes.objects.filter(
                            product__salePercent__gt=0
                        ).order_by("-product__price")[fistItem : fistItem + 12]
                    if price == 0:
                        clothes = Clothes.objects.filter(product__salePercent__gt=0)[
                            fistItem : fistItem + 12
                        ]
            # not sale
            else:
                # have cate
                if category != 0:
                    if price == 1:
                        clothes = Clothes.objects.filter(category=category).order_by(
                            "product__price"
                        )[fistItem : fistItem + 12]
                    if price == 2:
                        clothes = Clothes.objects.filter(category=category).order_by(
                            "-product__price"
                        )[fistItem : fistItem + 12]
                    if price == 0:
                        clothes = Clothes.objects.filter(category=category)[
                            fistItem : fistItem + 12
                        ]
                # not have cate
                else:
                    if price == 1:
                        clothes = Clothes.objects.all().order_by("product__price")[
                            fistItem : fistItem + 12
                        ]
                    if price == 2:
                        clothes = Clothes.objects.all().order_by("-product__price")[
                            fistItem : fistItem + 12
                        ]
            for c in clothes:
                images = ImageView.getListImage(c.product.product_id)
                product = {
                    "product_id": c.product.product_id,
                    "name": c.product.name,
                    "price": c.product.price,
                    "salePercent": c.product.salePercent,
                    "in_stock": c.product.in_stock,
                    "sold": c.product.sold,
                    "image": images,
                }
                data.append(
                    {
                        "clothes_id": c.clothes_id,
                        "category": c.category,
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
