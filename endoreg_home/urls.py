from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Dashboard'),
    path('annotationen/', views.about, name='annotationen'),
    path('video-annotation', views.video_annotation, name='video_annotation'),
    path('frame-annotation', views.frame_annotation, name='frame_annotation'),
    path('ueber-uns/', views.login, name='ueber-uns'),
    path('validierung/', views.validierung, name='validierung'),
    path('profil', views.profil, name='profil')
    ]
