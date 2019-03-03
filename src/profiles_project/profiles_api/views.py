from django.shortcuts import render

#from rest_framework.views module import APIView class
from rest_framework.views import APIView

#from rest_framework.response module import Response
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    '''test api view'''

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
