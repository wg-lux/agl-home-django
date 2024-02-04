from django.shortcuts import render

from logging import getLogger
logger = getLogger("my_oidc_backend")

# Create your views here.
def landing_page(request):
    # from django.contrib.sessions.models import Session
    # all_sessions = Session.objects.all()
    # logger.warning("REMOVING All Sessions:")

    # for session in all_sessions:
    #     logger.warning(session.get_decoded())
    #     session.delete()
    return render(request, "landing_page.html")