from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API view"""

    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of api views feature"""

        an_apiview = [
             'Uses HTTP as function (get, post, put , delete)',
             'Is Similar to a traditional Django View',
             'Gives you most control over your application logic ',
             'Is mapped manually to urls',
        ]

        return Response({'message':'Hello!','an_apiview': an_apiview})

    def post(self,request):
        """Create a hello message with our name"""

        serializers = self.serializers_class(data=request.data)

        if serializers.is_valid():
            name=serializer.validated_data.get('name')
            message= f'Hello{name}'
            return Response ({'message':message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle partial updating an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test Api Viewset"""
    serializer_class = serializers.HelloSerializer


    def list(self,request):
        """Return a hello message"""

        a_viewset = [
         'Uses function (list, create, update , partial_update)',
         'Automatically maps to urls using Routers',
         'Provides more functionality with less code',
         ]

        return Response({'message':'Hello!','a_viewset': a_viewset})

    def create(self,request):
        """Create a hello message with our name"""

        serializers = self.serializers_class(data=request.data)

        if serializers.is_valid():
            name=serializer.validated_data.get('name')
            message= f'Hello{name}'
            return Response ({'message':message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

            
    def retrieve(self,request,pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle updating part of an object by its ID"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an Object"""
        return Response({'http_method':'DELETE'})
