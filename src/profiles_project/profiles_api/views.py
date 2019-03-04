from django.shortcuts import render

#base model for all the viewsets django has
from rest_framework import viewsets

#from rest_framework.views module import APIView class
from rest_framework.views import APIView

#from rest_framework.response module import Response
from rest_framework.response import Response

#. imports from the root directory i.e profiles_project
from . import serializers

#imports status codes i.e 505, 404
from rest_framework import status

# Create your views here.

class HelloApiView(APIView):
    '''test api view'''

    #give the access of our serializer by giving the class name of our serializers.py file
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''returns a list of api view features'''

        an_apiview = [
        "uses HTTP methods as function (get, post, delete, patch, put)",
        " it is similar to traditional django view",
        "gives you most control over your logic",
        "it maps manually to URLs"
        ]

        #in APIView return is always in Response
        #Response should be a dictionary format
        return Response({"message":"hello", "an_apiview":an_apiview})

    def post(self, request):
        '''creates a hello  message with our name'''

        serializer = serializers.HelloSerializer(data=request.data)

        #validate the value entered as name
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "hello {0}".format(name)


            return Response({"message":message})

        else:

            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        '''handles updating an object and pk is primary key'''

        return Response({"method":"put"})

    def patch(self, request, pk=None):
        '''partially updates the object i.e only fields p   rovided in requests'''

        return Response({"method":"patch"})

    def delete(self, request, pk=None):
        ''' deletes an object'''

        return Response({"method":"delete"})

class HelloViewSet(viewsets.ViewSet):
    '''test api view set'''
    '''view set doesn't use traditional http methods for their function name'''

    serializer_class = serializers.HelloSerializer

    def list(self, request, format=None):
        '''return a hello message'''

        a_viewset = [
        "uses action(list, creates, update, retreive, partial_update)",
        "automatically maps to urls using routers",
        "proivdes more functionality with less code"
        ]

        return Response({"message":"Hello!", "a_viewset":a_viewset
        })

    def create(self, request):
        '''creates a new hello message'''

        #similar to post function of APIView
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "hello {0}".format(name)

            return Response({"mesasge":message})
        else:

            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    #make sure name of every function is correcct otherwise it gives error.
    def retrieve(self, request, pk=None):
        '''handles getting an object by it's ID'''

        return Response({"http_method":"GET"})

    def update(self, request, pk=None):
        '''pk for which objects need to be updated'''

        return Response({"http_method":"PUT"})

    def partial_update(self, request, pk=None):
        '''handles updating part of an object'''

        return Response({"http_method":"PATCH"})

    def destroy(self, request, pk=None):
        '''handles removing an object'''

        return Response({"http_method":"DELETE"})
