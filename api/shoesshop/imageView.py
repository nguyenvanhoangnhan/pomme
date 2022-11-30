from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, JSONParser
import cloudinary.uploader
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


class ImageView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    @staticmethod
    def post(request):
        urls = []
        # try:
        files = request.FILES.getlist("image")
        for f in files:
            upload_data = cloudinary.uploader.upload(f)
            urls.append(upload_data["url"])
        return Response(
            {
                "message": "success",
                "data": urls,
            },
            status=201,
        )
        # except:
        #     return Response({"message": "error", "data": []}, status=400)

    def createImage(data):
        serializer = ImageSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return

    def getListImage(idP):
        images = Image.objects.filter(product=idP)
        # serializer = ImageSerializer(instance=images, many=True)
        return images.values()
