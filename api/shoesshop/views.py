from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.models import User
from shoesshop.serializer import UserSerializer

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

