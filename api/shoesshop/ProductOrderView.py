from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework import generics
import cloudinary.uploader
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from shoesshop.models import (
    Shoe,
    Product,
    Image,
    Clothes,
    Accessory,
    UserCartProduct,
    UserLoveProduct,
    Order,
    OrderProduct
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
    OrderedSerializer,
    OrderProductSerializer,
    User_OrderSerializer,
    OrderSerializer
    
)


# User -> Order 
class UserOrderView(viewsets.ViewSet):
    serializer_class = User_OrderSerializer
    queryset = User.objects.all()
    @api_view(["GET"])
    def retrieve(self, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = User_OrderSerializer(instance=user)
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
   
    @api_view(["GET"])
    def list(self):
        users = User.objects.all()
        serializer = User_OrderSerializer(users,many = True)
        print(users)
        return Response(
            {
                "data": serializer.data,    
            },
            status=status.HTTP_200_OK,
        )
class OrderedProductList(APIView):
    def get(self,request):
        orders = Order.objects.all()
        serializer = OrderedSerializer(orders,many = True)
        return Response({
          "data" :   serializer.data
        },
            status= status.HTTP_200_OK
            )
    def post(self,request,format= None):
        serializer = OrderProductSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class OrderedProductDetail(APIView):
    def get(self,request,pk):
        order = get_object_or_404(Order,pk=pk)
        serializer = OrderedSerializer(order)
        return Response({
          "data" :   serializer.data
        },
            status= status.HTTP_200_OK
            )
    def delete(self,request,pk,format = None):
        order = get_object_or_404(Order,pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# CRUD Order 
class OrderView(viewsets.ViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "data": serializer.data,
                "message": "order Created Successfully",
            },
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, pk=None):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(instance=order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "data": serializer.data,
                "message": "order updated Successfully!",
            },
            status=status.HTTP_202_ACCEPTED,
        )

    def retrieve(self, request, pk=None):
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(instance=order)
            return Response(
                {
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "message": "order is invalid!",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def list(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(instance=orders, many=True)
        return Response(
            {
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )