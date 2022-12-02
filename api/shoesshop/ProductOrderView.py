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
    OrderSerializer,
    User_OrderSerializer,
    
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
class OrderProductList(APIView):
    def get(self,request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders,many = True)
        return Response({
          "data" :   serializer.data
        },
            status= status.HTTP_200_OK
            )
    def post(self,request,format= None):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class OrderProductDetail(APIView):
    def get(self,request,pk):
        order = get_object_or_404(Order,pk=pk)
        serializer = OrderSerializer(order)
        return Response({
          "data" :   serializer.data
        },
            status= status.HTTP_200_OK
            )
    def delete(self,request,pk,format = None):
        order = get_object_or_404(Order,pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    