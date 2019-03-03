from rest_framework import serializers

#from class serializers import Serializer object
class HelloSerializer(serializers.Serializer):
    '''Serializes a name field for testing our api view'''

    #serializers have a lot of predefined fields
    name = serializers.CharField(max_length=10)
