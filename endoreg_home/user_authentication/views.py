from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.conf import settings 
from django.urls import reverse
import logging

# Create a logger for your OIDC backend
logger = logging.getLogger('my_oidc_backend')



# Create your views here.
# KEYCLOAK_BASE_URL = 'https://keycloak.endo-reg.net/realms/master/protocol/openid-connect'
# ENDOREG_HOME_URL = 'https://home.endo-reg.net'

KEYCLOAK_BASE_URL = settings.KEYCLOAK_BASE_URL
ENDOREG_HOME_URL = settings.ENDOREG_HOME_URL

# @login_required
def user_status(request):
    user = request.user

    logger.warning("TRYING TO GET CUSTOM DATA")
    logger.warning(user.info)

    context = {
        'is_authenticated': user.is_authenticated,
        # 'roles': user.get_roles() if hasattr(user, 'get_roles') else [],
    }
    return render(request, 'user_status.html', context)

def keycloak_logout(request):
    # Here you can add any additional logout logic if needed
    # Construct the Keycloak logout URL
    keycloak_logout_url = (
        f"{KEYCLOAK_BASE_URL}/logout?redirect_uri={request.build_absolute_uri(reverse('landing_page'))}"
    )
    return redirect(keycloak_logout_url)

def force_reauth(request):
    # Optionally log out the user first
    django_logout(request)
    # Redirect to login URL, triggering OIDC flow
    return redirect(reverse(f'{KEYCLOAK_BASE_URL}/auth'))

def force_reauth(request):
    logger.info('Forcing re-authentication...')
    # log out the user first
    django_logout(request)
    # Clear all sessions
    ######################## REMOVE AFTER TESTING ############################
    from django.contrib.sessions.models import Session
    Session.objects.all().delete()  # This clears all sessions

    # redirect to landing_page
    return redirect(reverse('landing_page'))

# In your OIDC or authentication view
def my_oidc_login_response_view(request):
    # This assumes you have access to the request session or a similar mechanism
    id_token = request.session.get('oidc_id_token')
    if id_token:
        logger.debug(f"ID Token found in session: {id_token}")
    else:
        logger.debug("No ID Token found in session.")

def redirect_after_logout(request):
    # LOG ALL GLOBALLY AVAILABLE REMAINING SESSIONS TO DEBUG
    

    # Redirect to your app's landing page

    return redirect(ENDOREG_HOME_URL)
        
# def custom_logout(request):
#     # Log out the user from Django session
#     print("LOGGING OUT OF DJANGO")
#     django_logout(request)
#     # Construct the Keycloak logout URL with redirect URI back to your app
#     keycloak_logout_url = f"https://your-keycloak-domain/auth/realms/your-realm-name/protocol/openid-connect/logout?redirect_uri=http://localhost:8000/"
#     # Redirect to Keycloak logout URL
#     return redirect(keycloak_logout_url)

