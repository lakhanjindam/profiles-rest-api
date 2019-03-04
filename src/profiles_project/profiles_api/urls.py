from django.conf.urls import include

#from router class import DefaultRouter
from rest_framework.routers import DefaultRouter

from django.conf.urls import url

from .import views

#creating router object
router = DefaultRouter()

#1st parameter is name of viewset and 2nd is the registered class name of our viewset in views.py
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

#it firsts checks for the first url, if entered url doesn't match the first then goes to second url.
urlpatterns = [
    url(r'^hello-view', views.HelloApiView.as_view()),
    url(r'', include(router.urls))
]
