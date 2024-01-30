# forms.py in your main app
#
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from agl_base_db.models import PortalUserInfo

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


PortalUserInfoForm = forms.ModelForm

# class PortalUserInfoForm(forms.ModelForm):
#     class Meta:
#         model = PortalUserInfo
#         fields = ['profession', 'works_in_endoscopy']
#         # Include other fields as needed
