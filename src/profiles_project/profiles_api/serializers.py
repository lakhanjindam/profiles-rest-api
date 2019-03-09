from rest_framework import serializers
from . import models

#from class serializers import Serializer object and is a base serializer.
class HelloSerializer(serializers.Serializer):
    '''Serializes a name field for testing our api view'''

    #serializers have a lot of predefined fields
    name = serializers.CharField(max_length=10)


#creating a model serializer for our user profiles.
class UserProfileSerializer(serializers.ModelSerializer):
     '''a serializer for user profile object'''

     #creating meta data for our class to access it from models.py file.
     class Meta:
         #here accessing UserProfile class from models.py
         model = models.UserProfile
         fields = ('id','email','name','password')
         #add this extra field for password so that one cannot read passwords
         extra_kwargs = {
         'password':{'write_only':True}
         }


     def  create(self, validated_data):

         '''create and return new user'''

         #creates a profile in the basis of name and email.
         user = models.UserProfile(
         email=validated_data['email'],
         name=validated_data['name'],
         )

         #setting password
         user.set_password(validated_data['password'])
         user.save()

         return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    '''a serializer for profile-feed-item'''

    class Meta:

        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')

        #set this so that users can only read feeds of other users.
        extra_kwargs = {
        'user_profile':{'read_only':True}

        }
