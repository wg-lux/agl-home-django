import os

KEYCLOAK_BASE_URL = 'https://keycloak.endo-reg.net/realms/master/protocol/openid-connect'
ENDOREG_HOME_URL = 'https://home.endo-reg.net'


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ADD mozilla_django_oidc.middleware.SessionRefresh to MIDDLEWARE

OIDC_RP_CLIENT_ID = os.environ.get('KEYCLOAK_CLIENT', 'agl-home-django')
OIDC_RP_CLIENT_SECRET = os.environ.get('KEYCLOAK_SECRET', 'agl-home-django') #TODO make production safe

# The URL of your Keycloak server, with your realm name
OIDC_OP_AUTHORIZATION_ENDPOINT = f'{KEYCLOAK_BASE_URL}/auth'
OIDC_OP_TOKEN_ENDPOINT = f'{KEYCLOAK_BASE_URL}/token'
OIDC_OP_USER_ENDPOINT = f'{KEYCLOAK_BASE_URL}/userinfo'

OIDC_OP_JWKS_ENDPOINT = f'{KEYCLOAK_BASE_URL}/certs'
OIDC_RP_SIGN_ALGO = 'RS256'  # Keycloak's default signing algorithm

OIDC_RP_SCOPES = 'openid email roles open_id_role_list' # offline_access'

# Where to redirect after successful authentication
LOGIN_REDIRECT_URL = "/"

# Where to redirect after logout
LOGOUT_REDIRECT_URL = "/redirect-after-logout/"
ALLOW_LOGOUT_GET_METHOD = True

AUTHENTICATION_BACKENDS = [
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
    'user_authentication.models.MyOIDCBackend',
    # "rest_framework.authentication.SessionAuthentication"
]

##### Other settings
# Auto Create User
OIDC_CREATE_USER = True

# session key stores OIDC access_token as store data oidc_access_token
# Potential security risk if not set to False
OIDC_STORE_ACCESS_TOKEN = False

OIDC_RP_RESPONSE_TYPE = 'code'

# session key stores OIDC id_token as store data oidc_id_token
OIDC_STORE_ID_TOKEN = True

# Potential security risk if not set to False
OIDC_ALLOW_UNSECURED_JWT = True

# Default Renew ID Token Expiry Seconds, default is 15 minutes
OIDC_RENEW_ID_TOKEN_EXPIRY_SECONDS = 60 * 15



##########################################################################

# OIDC_STORE_ID_TOKEN = True
# OIDC_ID_TOKEN_PROCESSING_HOOK = 'endoreg_home.settings.jwt_decoder'




# OIDC_OP_LOGOUT_ENDPOINT = f'{KEYCLOAK_BASE_URL}/logout'

