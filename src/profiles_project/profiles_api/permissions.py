from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    '''alllows users to update their own profile'''

    def has_object_permission(self, request, view, obj):
        '''check if user is trying to edit their own profile'''

        #if user wants to view a profile.
        #SAFE_METHODS allows users only to retrieve data and not change it.
        #it's  an HTTP GET method.  
        if request.method in permissions.SAFE_METHODS:
            return True

        #checks whether id user is going to change has same id as the user
        #that currently authenticated in system.
        return obj.id==request.user.id
