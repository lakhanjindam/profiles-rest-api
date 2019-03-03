# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


'''UserProfileManager name should be same as class name'''
class UserProfileManager(BaseUserManager):
    '''helps django works with our custom user models'''
    def create_user(self, email, name, password=None):
        '''creates a new user profile'''

        '''checks the eamil exist or not'''
        if not email:

            '''pops an error with a xustom message'''
            raise ValueError("users must  have an email address")

        '''it converts the email into a standardized format'''
        email = self.normalize_email(email)

        '''creates a new user profile model as a object'''
        user = self.model(email=email, name=name)

        '''password setting and it encrypts the password  in hash code '''
        user.set_password(password)

        '''saves user profiles in same db we created'''
        user.save(using=self.db)

        return user

    '''here in password dont add none value bocz we need password to access the super user'''
    def create_super_user(self, email, name, password):
        '''creates and save a new super user wuth given details'''
        '''super user has full control in a system like an admin'''

        '''creates an user by calling above function'''
        user = self.create_user(email, name, password)

        '''to allow access to superuser and as a staff member'''
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self.db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """docstring for UserProfile.represents a user profile in our system"""
    '''unique is used to check the email is unique everytime user signup'''

    email = models.EmailField(max_length=255, unique=True)

    '''for name character is used'''
    name = models.CharField(max_length=255)

    '''it determines whether user is currently active or not'''
    is_active = models.BooleanField(default=True)

    '''bcoz we dont want new members coming in as a staff member'''
    is_staff = models.BooleanField(default=False)

    ''''it  can be used to manage the user profiles objects in django'''
    '''built in function of django'''
    objects = UserProfileManager()


    USERNAME_FIELD = 'email'

    '''list of things u wanted to be required'''
    '''only add name as email is alreaady in required by the system'''
    REQUIRED_FIELD = ['name']

    '''now create helper functions'''

    def get_full_name(self):
        '''used to get users full name'''

        return self.name

    def get_short_name(self):
        '''used to get  users short name, u can also do it for getting last name and first name'''

        return self.name

    def __str__(self):
        '''this is used to when django needs to convert an objects to strings'''

        return self.email
