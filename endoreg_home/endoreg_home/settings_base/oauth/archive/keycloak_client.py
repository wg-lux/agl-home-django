from keycloak import KeycloakOpenID
import os
from ..base_urls import KEYCLOAK_BASE_URL, KEYCLOAK_REALM_BASE_URL, ENDOREG_HOME_URL

# Get environment variables
CLIENT_ID = os.environ.get('KEYCLOAK_CLIENT', 'test_client')
CLIENT_SECRET = os.environ.get('KEYCLOAK_SECRET', 'such-secrecy-wooooow') #TODO make

# Configure URLS
# The URL of your Keycloak server, with your realm name
AUTHORIZATION_ENDPOINT = f'{KEYCLOAK_REALM_BASE_URL}/auth'
TOKEN_ENDPOINT = f'{KEYCLOAK_REALM_BASE_URL}/token'
USER_ENDPOINT = f'{KEYCLOAK_REALM_BASE_URL}/userinfo'
JWKS_ENDPOINT = f'{KEYCLOAK_REALM_BASE_URL}/certs'
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/redirect-after-logout/"

# Other Settings:
SIGN_ALGO = 'RS256'
SCOPES = 'openid email roles open_id_role_list'

# Configure client
keycloak_openid = KeycloakOpenID(server_url=KEYCLOAK_BASE_URL,
                                 client_id=CLIENT_ID,
                                 realm_name="master",
                                 client_secret_key=CLIENT_SECRET)

# Get WellKnown
config_well_known = keycloak_openid.well_known()

# Get Code With Oauth Authorization Request
auth_url = keycloak_openid.auth_url(
    redirect_uri=LOGIN_REDIRECT_URL,
    scope=SCOPES,
    state="your_state_info")

#########################################################################################################
keycloak_openid = KeycloakOpenID(server_url="https://keycloak.endo-reg.net",
                                 client_id="agl-home-django",
                                 realm_name="master",
                                 client_secret_key="2tkBiwvwIIJEofbQqiGcmzw1T3eiJZK0")

# https://keycloak.endo-reg.net/realms/master/protocol/openid-connect