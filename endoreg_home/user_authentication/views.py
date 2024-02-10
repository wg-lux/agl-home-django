from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse


# Create a logger for your OIDC backend
# Create your views here.
KEYCLOAK_BASE_URL = 'https://keycloak.endo-reg.net/realms/master/protocol/openid-connect'
ENDOREG_HOME_URL = 'https://home.endo-reg.net'

# KEYCLOAK_BASE_URL = settings.KEYCLOAK_BASE_URL
# ENDOREG_HOME_URL = settings.ENDOREG_HOME_URL


def in_specific_group(user):
    return user.groups.filter(name='user-intern').exists()

@user_passes_test(in_specific_group)
def test_auth_view(request):
    # View logic
    return HttpResponse('This is a protected view')


# @login_required
def user_status(request):
    user = request.user

    context = {
        'is_authenticated': user.is_authenticated,
        # 'roles': user.get_roles() if hasattr(user, 'get_roles') else [],
    }
    return render(request, 'user_status.html', context)

def redirect_after_logout(request):
    # LOG ALL GLOBALLY AVAILABLE REMAINING SESSIONS TO DEBUG
    

    # Redirect to your app's landing page

    return redirect(ENDOREG_HOME_URL)
        