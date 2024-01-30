from django.shortcuts import render, redirect
from ..forms import RegisterForm, PortalUserInfoForm
# from agl_base_db.models import PortalUserInfo
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required

##### Doc views #####
from .documentation import (
    documentation_main,
)

########### How to assign groups to users ############
# user is a django user
# demo_group = Group.objects.get(name='demo')
# demo_group.user_set.add(new_user)

########### How to assign permissions to groups ############
# from django.contrib.auth.models import Permission
# permission = Permission.objects.get(codename='specific_permission_codename')
# verified_group = Group.objects.get(name='verified')
# verified_group.permissions.add(permission)

########### HOW TO CHECK PERMISSIONS ############
# from django.contrib.auth.decorators import login_required, permission_required

# @login_required
# @permission_required('app_label.permission_codename', raise_exception=True)
# def some_view(request):
#     # View logic here


def landing_page(request):
    return render(request, 'landing_page.html')

def register(request):
    pass
    # if request.method == 'POST':
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         new_user = form.save()
    #         demo_group = Group.objects.get(name='demo')
    #         demo_group.user_set.add(new_user)
    #         PortalUserInfo.objects.create(user=new_user)  # Create PortalUserInfo instance
    #         return redirect('landing_page')
    # else:
    #     form = RegisterForm()
    # return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    pass
    # if request.method == 'POST':
    #     form = PortalUserInfoForm(request.POST, instance=request.user.portaluserinfo)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('profile')
    # else:
    #     try:
    #         form = PortalUserInfoForm(instance=request.user.portaluserinfo)
    #     except PortalUserInfo.DoesNotExist:
    #         PortalUserInfo.objects.create(user=request.user)
    #         form = PortalUserInfoForm(instance=request.user.portaluserinfo)

    # return render(request, 'profile.html', {'form': form})

