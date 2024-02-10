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
    # logger.debug("----PRE SOCIAL LOGIN CALLED----")
    # logger.debug(f"Social login data: {sociallogin.account.extra_data}")
    keycloak_groups = sociallogin.account.extra_data.get('groups', [])
    
    user = sociallogin.user

    if user.id:
        user.groups.clear()

    # Assign new roles from Keycloak
    for role_name in keycloak_groups:
        group, _ = Group.objects.get_or_create(name=role_name)
        user.groups.add(group)

    if 'admin' in keycloak_groups:
        user.is_staff = True
        user.is_superuser = True
        user.save()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    keycloak_roles = models.TextField()

    def __str__(self):
        return self.user.username
