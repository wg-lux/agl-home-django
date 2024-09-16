import os
import json
from .django_settings import *
from ..base_urls import KEYCLOAK_BASE_URL, KEYCLOAK_REALM_BASE_URL

# Get environment variables

CLIENT_ID_PATH = os.environ.get('KEYCLOAK_CLIENT_PATH', 'keycloak_client_id')
CLIENT_SECRET_PATH = os.environ.get('KEYCLOAK_SECRET_PATH', 'keycloak_client_secret')

with open("test-log.txt", "w") as f:
    f.write(f"CLIENT_ID_PATH: {CLIENT_ID_PATH}\n")
    f.write(f"CLIENT_SECRET_PATH: {CLIENT_SECRET_PATH}\n")

try:
    with open(CLIENT_ID_PATH, 'r') as f:
        CLIENT_ID = f.read().strip()
    with open(CLIENT_SECRET_PATH, 'r') as f:
        CLIENT_SECRET = f.read().strip()

except FileNotFoundError:
    CLIENT_ID = os.environ.get('KEYCLOAK_CLIENT', 'test_client')
    CLIENT_SECRET = os.environ.get('KEYCLOAK_SECRET', 'such-secrecy-wooooow') #TODO make

AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
]

USERSESSIONS_TRACK_ACTIVITY = True # Requires allauth.usersessions.middleware.UserSessionsMiddleware
USERSESSIONS_ADAPTER = "allauth.usersessions.adapter.DefaultUserSessionsAdapter" # is default

SOCIALACCOUNT_ADAPTER = 'user_authentication.adapters.CustomSocialAccountAdapter'

SOCIALACCOUNT_PROVIDERS = {
    "openid_connect": {
        "APPS": [
            {
                "provider_id": "keycloak",
                "name": "Keycloak",
                "client_id": CLIENT_ID,
                "secret": CLIENT_SECRET,
                "settings": {
                    "server_url": f"{KEYCLOAK_BASE_URL}/realms/master/.well-known/openid-configuration",
                },
            }
        ]
    }
}


LOGIN_REDIRECT_URL = "landing_page"
LOGOUT_REDIRECT_URL = "landing_page"

