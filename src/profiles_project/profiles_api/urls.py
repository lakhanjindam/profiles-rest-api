from django.conf.urls import url

from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from .import views

#creating router object
router = DefaultRouter()

#1st parameter is name of viewset and 2nd is the registered class name of our viewset in views.py
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

#when creating a model viewset no need to add base_name in URLs,
#django rest_framework automatically figures this out by looking at model specified
router.register('profile', views.UserProfileViewSet)

#here base_name is required bcoz it is not a model view set and we need to tell django it's base_name.
router.register('login', views.LoginViewSet, base_name='login')

#model ViewSet no need to specify a base_name.
router.register('feed', views.UserProfileFeedViewSet)

#it firsts checks for the first url, if entered url doesn't match the first then goes to second url.
urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls))
]
