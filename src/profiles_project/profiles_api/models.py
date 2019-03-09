from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

#UserProfileManager is already built-in model of django rest_framework.
class UserProfileManager(BaseUserManager):
    """Class required by Django for managing our users from the management
    command.
    """

    def create_user(self, email, name, password=None):
        """Creates a new user with the given detials."""

        # Check that the user provided an email.
        if not email:
            raise ValueError('Users must have an email address.')

        # Create a new user object.
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        # Set the users password. We use this to create a password
        # hash instead of storing it in clear text.
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given detials."""

        # Create a new user with the function we created above.
        user = self.create_user(
            email,
            name,
            password
        )

        # Make this user an admin.
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """A user profile in our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)#for super admin access.

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Required function so Django knows what to use as the users full name.
        """

        self.name

    def get_short_name(self):
        """
        Required function so Django knows what to use as the users short name.
        """

        self.name

    def __str__(self):
        """What to show when we output an object as a string."""

        return self.email

#it's like an custom model unlike other models we described above.
#models.Model is a base for creating any model.
class ProfileFeedItem(models.Model):
    '''updates profile feed item'''

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    #to add text in status field.
    #Note: CharField always require a max_length attribute, 255 is max char limit.
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    '''last step is to convert a model object into string'''

    def __str__(self):
        '''returns our model as striing as an ouput.'''

        return self.status_text
