from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.models import User
from shoesshop.models import Shoe
from shoesshop.serializer import ShoeSerializer, UserSerializer

class UserView(viewsets.ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def create(self, request, *args,  **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "data": serializer.data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        },status=status.HTTP_201_CREATED)
    def update(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(instance=user,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "data": serializer.data,     
            "message": "User updated Successfully!",      
        },status=status.HTTP_202_ACCEPTED)
    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)    
            serializer = UserSerializer(instance=user)
            return Response({
                "data": serializer.data,           
            },status=status.HTTP_200_OK)
        except:    
            return Response({
                    "message": 'user is invalid!',           
                },status=status.HTTP_400_BAD_REQUEST)
       
    def list(self,request):
        users = User.objects.all()
        serializer = UserSerializer(instance=users,many=True)
        return Response({
            "data": serializer.data,           
        },status=status.HTTP_200_OK)
# # Cách 1: Ngắn gọn nhất 
# class ShoeView(viewsets.ModelViewSet):
#     serializer_class = ShoeSerializer
#     queryset = Shoe.objects.all()

class ShoeView(viewsets.ViewSet):
    serializer_class = ShoeSerializer
    queryset = Shoe.objects.all()
    def retrieve(self, request, pk=None):
        try:
            shoe = Shoe.objects.get(pk=pk)    
            serializer = ShoeSerializer(instance=shoe)
            return Response({
                "data": serializer.data,           
            },status=status.HTTP_200_OK)
        except:    
            return Response({
                    "message": 'Shoe not found!',           
                },status=status.HTTP_400_BAD_REQUEST)
       
    def list(self,request):
        shoes = Shoe.objects.all()
        serializer = ShoeSerializer(instance=shoes,many=True)
        return Response({
            "data": serializer.data,           
        },status=status.HTTP_200_OK)
        
    def create(self, request, *args,  **kwargs):
        serializer = ShoeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "data": serializer.data,
            "message": "Shoe Created Successfully!",
        },status=status.HTTP_201_CREATED)
    def update(self, request, pk=None):
        shoe = Shoe.objects.get(pk=pk)
        serializer = ShoeSerializer(instance=shoe,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "data": serializer.data,     
            "message": "Shoe updated Successfully!",      
        },status=status.HTTP_202_ACCEPTED)
    
    def destroy(self, request,pk=None):
        # delete an object and send a confirmation response
        try:
            Shoe.objects.get(pk=pk).delete()
            return Response({"message": "Shoe delete Successfully!",      
            },status=status.HTTP_200_OK)
        except:
            
            return Response({"message": "Shoe not found!",      
            },status=status.HTTP_404_NOT_FOUND)