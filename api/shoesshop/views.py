from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, JSONParser
import cloudinary.uploader
from rest_framework import status, viewsets
from django.contrib.auth.models import User
from shoesshop.models import Shoe, Product, Image
from shoesshop.serializer import (
    ShoeSerializer,
    UserSerializer,
    ProductSerializer,
    ImageSerializer,
)


class UserView(viewsets.ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, data):
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "data": serializer.data,
                "message": "User Created Successfully",
            },
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "data": serializer.data,
                "message": "User updated Successfully!",
            },
            status=status.HTTP_202_ACCEPTED,
        )

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(instance=user)
            return Response(
                {
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "user is invalid!",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(instance=users, many=True)
        return Response(
            {
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


# # Cách 1: Ngắn gọn nhất
# class ShoeView(viewsets.ModelViewSet):
#     serializer_class = ShoeSerializer
#     queryset = Shoe.objects.all()

# -----------------------------upload image to cloud--------------------


class ImageView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    @staticmethod
    def post(request):
        urls = []
        try:
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
        except:
            return Response({"message": "error", "data": []}, status=400)

    def createImage(data):
        serializer = ImageSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return

    def getListImage(idP):
        images = Image.objects.filter(product=idP)
        # serializer = ImageSerializer(instance=images, many=True)
        return images.values()


# -------------------------------------------------------------------


class ProductView(viewsets.ViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def createProduct(self, data):
        serializer = ProductSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        return serializer["product_id"].value


# -----------------shoe view------------------------------------------


class ShoeView(viewsets.ViewSet):
    serializer_class = ShoeSerializer
    queryset = Shoe.objects.all()

    def retrieve(self, request, pk=None):
        try:
            shoe = Shoe.objects.get(pk=pk)
            serializer = ShoeSerializer(instance=shoe)
            return Response(
                {
                    "data": serializer.data,
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
        page = page
        fistItem = (page - 1) * 12
        data = []
        shoes = Shoe.objects.all()[fistItem : fistItem + 12].select_related("product")
        for s in shoes:
            images = ImageView.getListImage(s.product.product_id)
            print(images)
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

    def create(self, request, *args, **kwargs):
        try:
            product = ProductView.createProduct(request.data["product"])
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

    def destroy(self, request, pk=None):
        # delete an object and send a confirmation response
        try:
            Shoe.objects.get(pk=pk).delete()
            return Response(
                {
                    "message": "Shoe delete Successfully!",
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Shoe not found!",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
