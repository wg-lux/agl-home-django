# urls.py

from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('user-status/', views.user_status, name='user_status'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('keycloak-logout/', views.keycloak_logout, name='keycloak_logout'),
    path("force-reauth/", views.force_reauth, name="force_reauth"),
    path("redirect-after-logout/", views.redirect_after_logout, name="redirect_after_logout"),
]
