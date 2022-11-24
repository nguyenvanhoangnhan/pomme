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


class UserView(viewsets.ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        serializer = UserSerializer(data=request.data)
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


# -------------------------------Product view------------------------------------


# -------------------------------Shoe view------------------------------------------


# -------------------------------Clothes view--------------------------------------


# ------------------------------Accessory view----------------------------------


# -------------------------------USER CART PRODUCT VIEW -------------------------------------
class UserCartProductView(viewsets.ViewSet):
    queryset = UserCartProduct.objects.all()

    def list(self, request):
        user_id = request.query_params.get("user_id")
        if user_id is not None:
            cart = UserCartProduct.objects.filter(user_id=user_id)
        else:
            cart = UserCartProduct.objects.all()
        serializer = UserCartProductSerializer(instance=cart, many=True)
        return Response(
            {"data": serializer.data},
            status=status.HTTP_404_NOT_FOUND,
        )

    def retrieve(self, request, pk=None):
        try:
            cart = UserCartProduct.objects.get(pk=pk)
            serializer = UserCartProductSerializer(instance=cart)
            return Response(
                {
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Cart item not found!",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def create(self, request):
        serializer = CartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "data": serializer.data,
                "message": "Cart item Created Successfully!",
            },
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, pk=None):
        cart = UserCartProduct.objects.get(pk=pk)
        serializer = CartSerializer(instance=cart, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "data": serializer.data,
                "message": "Cart item updated Successfully!",
            },
            status=status.HTTP_202_ACCEPTED,
        )

    def destroy(self, request, pk=None):
        # delete an object and send a confirmation response
        try:
            UserCartProduct.objects.get(pk=pk).delete()
            return Response(
                {
                    "message": "Cart item delete Successfully!",
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Cart item not found!",
                },
                status=status.HTTP_404_NOT_FOUND,
            )


# --------------------------------------------------------
class UserLoveProductView(viewsets.ViewSet):
    queryset = UserLoveProduct.objects.all()

    def list(self, request):
        user_id = request.query_params.get("user_id")
        if user_id is not None:
            love = UserLoveProduct.objects.filter(user_id=user_id)
        else:
            love = UserLoveProduct.objects.all()
        serializer = UserLoveProductSerializer(instance=love, many=True)
        return Response(
            {"data": serializer.data},
            status=status.HTTP_404_NOT_FOUND,
        )

    def retrieve(self, request, pk=None):
        try:
            love = UserLoveProduct.objects.get(pk=pk)
            serializer = UserLoveProductSerializer(instance=love)
            return Response(
                {
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "Cart item not found!",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def create(self, request):
        data = request.data
        serializer = LoveSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "data": serializer.data,
                "message": "Cart item Created Successfully!",
            },
            status=status.HTTP_201_CREATED,
        )

    def destroy(self, request, pk=None):
        # delete an object and send a confirmation response
        try:
            UserLoveProduct.objects.get(pk=pk).delete()
            return Response(
                {
                    "message": "User Love product delete Successfully!",
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "User Love product not found!",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
