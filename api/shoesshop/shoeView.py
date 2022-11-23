from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, JSONParser
import cloudinary.uploader
from .imageView import ImageView
from .productView import ProductView
from rest_framework import status, viewsets
from django.contrib.auth.models import User
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


class ShoeView(viewsets.ViewSet):
    serializer_class = ShoeSerializer
    queryset = Shoe.objects.all()

    def retrieve(self, request, pk=None):
        try:
            shoe = Shoe.objects.get(pk=pk)
            images = ImageView.getListImage(shoe.product.product_id)
            product = {
                "product_id": shoe.product.product_id,
                "name": shoe.product.name,
                "price": shoe.product.price,
                "salePercent": shoe.product.salePercent,
                "in_stock": shoe.product.in_stock,
                "sold": shoe.product.sold,
                "image": images,
            }
            data = {
                "shoe_id": shoe.shoe_id,
                "gender": shoe.gender,
                "series": shoe.series,
                "shape": shoe.shape,
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
                    "message": "Shoe not found!",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    @api_view(["GET"])
    def getListShoe(self, page=None):
        try:

            page = page
            fistItem = (page - 1) * 12
            data = []
            shoes = Shoe.objects.all()[fistItem : fistItem + 12].select_related(
                "product"
            )
            for s in shoes:
                images = ImageView.getListImage(s.product.product_id)
                product = {
                    "product_id": s.product.product_id,
                    "name": s.product.name,
                    "price": s.product.price,
                    "salePercent": s.product.salePercent,
                    "in_stock": s.product.in_stock,
                    "sold": s.product.sold,
                    "image": images,
                }
                data.append(
                    {
                        "shoe_id": s.shoe_id,
                        "gender": s.gender,
                        "series": s.series,
                        "shape": s.shape,
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

    def create(self, request, *args, **kwargs):
        try:
            product = ProductView.createProduct(request.data["product"], 1)
            for img in request.data["image"]:
                image = {
                    "product": product,
                    "url": img["url"],
                    "is_thumbnail": img["is_thumbnail"],
                }
                ImageView.createImage(image)
            data = {
                "product": product,
                "gender": request.data["shoe"]["gender"],
                "series": request.data["shoe"]["series"],
                "shape": request.data["shoe"]["shape"],
            }
            serializer = ShoeSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "message": "Shoe Created Successfully!",
                },
                status=status.HTTP_201_CREATED,
            )
        except:
            return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        shoe = Shoe.objects.get(pk=pk)
        serializer = ShoeSerializer(instance=shoe, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "data": serializer.data,
                "message": "Shoe updated Successfully!",
            },
            status=status.HTTP_202_ACCEPTED,
        )
