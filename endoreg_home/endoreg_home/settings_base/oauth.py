KEYCLOAK_BASE_URL = 'https://keycloak.endo-reg.net/realms/master/protocol/openid-connect'
ENDOREG_HOME_URL = 'https://home.endo-reg.net'


# Custom OIDC_OP_USER_ENDPOINT to include roles in the user info
def jwt_decoder(token):
    import jwt  # PyJWT
    r = jwt.decode(token, verify=False)
    print('JWT DECODED')
    print(r)
    return r

OIDC_STORE_ID_TOKEN = True
OIDC_ID_TOKEN_PROCESSING_HOOK = 'endoreg_home.settings.jwt_decoder'


AUTHENTICATION_BACKENDS = [
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]

OIDC_RP_CLIENT_ID = 'agl-home-django'
OIDC_RP_CLIENT_SECRET = '2tkBiwvwIIJEofbQqiGcmzw1T3eiJZK0' #TODO make production safe
OIDC_OP_AUTHORIZATION_ENDPOINT = f'{KEYCLOAK_BASE_URL}/auth'
OIDC_OP_TOKEN_ENDPOINT = f'{KEYCLOAK_BASE_URL}/token'
OIDC_OP_USER_ENDPOINT = f'{KEYCLOAK_BASE_URL}/userinfo'
OIDC_OP_JWKS_ENDPOINT = f'{KEYCLOAK_BASE_URL}/certs'
OIDC_RP_SIGN_ALGO = 'RS256'
OIDC_RP_SCOPES = 'openid email'

LOGIN_REDIRECT_URL = 'https://home.endo-reg.net/'
LOGOUT_REDIRECT_URL = 'https://home.endo-reg.net/'
