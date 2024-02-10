from django.contrib.auth.models import User, Group
from django.db import models
from allauth.account.signals import user_logged_in
from django.dispatch import receiver

from allauth.socialaccount.signals import pre_social_login

import logging

logger = logging.getLogger("authentication")

@receiver(pre_social_login)
def handle_keycloak_roles(sender, request, sociallogin, **kwargs):
    # Assuming the roles are in sociallogin.account.extra_data['roles']
    logger.debug("----PRE SOCIAL LOGIN CALLED----")
    logger.debug(f"Social login data: {sociallogin.account.extra_data}")
    keycloak_groups = sociallogin.account.extra_data.get('groups', [])
    
    user = sociallogin.user

    # # Check if the user is already in the database
    if user.id:
        # User exists, so we might update their roles
        # Clear existing groups if you want to synchronize roles each time
        user.groups.clear()

    # Assign new roles from Keycloak
    for role_name in keycloak_groups:
        group, _ = Group.objects.get_or_create(name=role_name)
        user.groups.add(group)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    keycloak_roles = models.TextField()

    def __str__(self):
        return self.user.username
