from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from mozilla_django_oidc.auth import OIDCAuthenticationBackend

import logging

# Create a logger for your OIDC backend
logger = logging.getLogger('my_oidc_backend')
logger.info('Authentication Backend initializing...')


class UserInformation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='info')
    email = models.EmailField(max_length=254)
    roles = models.TextField()
    # Add any other fields you might need

    def __str__(self):
        return self.user.username

# import django abstract user model
from django.contrib.auth.models import AbstractUser

class MyOIDCBackend(OIDCAuthenticationBackend):
    logger.info('MyOIDCBackend initializing...')
    def verify_claims(self, claims):
        logger.debug("Custom verify_claims method called")
        logger.debug("Claims:")
        logger.debug(claims)

        verified = super(MyOIDCBackend, self).verify_claims(claims)
        # is_admin = 'admin' in claims.get('group', [])
        # openid email roles open_id_role_list offline_access
        return verified

    def create_user(self, claims):
        user = super(MyOIDCBackend, self).create_user(claims)
        user.email = claims.get('email')
        user.first_name = claims.get('given_name', '')
        
        user.save()
        # Create the UserInformation instance
        roles = claims.get('roles', '')  # Assuming roles are a space-separated string
        UserInformation.objects.create(user=user, email=user.email, roles=roles)
        return user

    def update_user(self, user, claims):
        logger.warning("Custom update_user method called")
        logger.warning("Claims:")
        logger.warning(claims)

        user.email = claims.get('email')
        user.first_name = claims.get('given_name', '')
        user.save()

        # For Debugging purposes, write the claims to tmp.json
        import json
        with open('user_tmp.json', 'w') as f:
            json.dump({
                'username': user.username,
                'email': user.email,
                # Add any other fields you're interested in
            }, f)

        # Update the UserInformation instance
        info, created = UserInformation.objects.get_or_create(user=user)
        info.email = user.email
        info.roles = claims.get('roles', '')  # Update roles
        info.save()
        return user

    def authenticate(self, *args, **kwargs):
        logger.debug("Custom authenticate method called")
        # Your custom authentication logic here
        return super().authenticate(*args, **kwargs)

    def filter_users_by_claims(self, claims):
        """Override to match users by email or another preferred method."""
        email = claims.get('email')
        if not email:
            return self.UserModel.objects.none()
        return self.UserModel.objects.filter(email=email)

