from rest_framework import permissions

#use BasePermission object from permissions class.
class UpdateOwnProfile(permissions.BasePermission):
    '''alllows users to update their own pro6file'''

    def has_object_permission(self, request, view, obj):
        '''check if user is trying to edit their own profile'''

        #if user wants to view a profile.
        #SAFE_METHODS allows users only to retrieve data and not change it.
        #it's  an HTTP GET method.
        if request.method in permissions.SAFE_METHODS:
            return True

        #checks whether id user that's going to update has same id as the user
        #that currently authenticated in system.
        return obj.id==request.user.id
