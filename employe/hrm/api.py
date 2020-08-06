from rest_framework.views import APIView #It contain get, put, post methode
from rest_framework.response import Response
from rest_framework import status
from hrm.serializer import *


class UserList(APIView):
    def get(self, request):
        model = User.objects.all()
        serializer = Userserializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get_id(self, employee_id):
        try:
            model = User.objects.get(id=employee_id)
            return model
        except User.DoesNotExist:
            return Response('User is Not Found in database',status=status.HTTP_404_NOT_FOUND)

    def get(self, request, employee_id):
        try:
            model = User.objects.get(id=employee_id)
        except User.DoesNotExist:
            return Response('User is Not Found in database',status=status.HTTP_404_NOT_FOUND)
        serializer = Userserializer(model)
        return Response(serializer.data)
    
    def put(self, request, employee_id):
        try:
            model = User.objects.get(id=employee_id)
        except User.DoesNotExist:
            return Response('User is Not Found in database',status=status.HTTP_404_NOT_FOUND)
        serializer = Userserializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, employee_id):
        model = self.get_id(employee_id)
        model.delete()
        return Response('User deleted successfully.', status=status.HTTP_400_BAD_REQUEST)