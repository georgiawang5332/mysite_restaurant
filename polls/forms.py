from django import forms
# 註冊 method : csirpy_form
from django.contrib.auth import login, authenticate
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# from polls.models import *
class EditForm(UserChangeForm):
  class Meta:
    model = User
    fields = [
      'email',
      'first_name',
      'last_name',
      'password',
    ]


# class RegistrationForm(UserCreationForm):
#   email = forms.EmailField(required=True)
#
#   class Meta:
#     model = User
#     fields = [
#       'username',
#       'first_name',
#       'last_name',
#       'email',
#       'password1',
#       'password2',
#     ]

# def save(self, commit=True):
#   user = super(UserCreationForm, self).save(commit=False)
#   user.first_name = self.cleaned_data['first_name']
#   user.last_name = self.cleaned_data['last_name']
#   user.email = self.cleaned_data['email']

#   if commit:
#     user.save()
#   return user

# part 16
class RegistrationForm(UserCreationForm):
  # email = forms.EmailField(max_length=60, help_text='必需的。 添加有效的電子郵件地址')

  class Meta:
    model = User
    # model = Store
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

#   USERNAME_FIELD = 'email'
# “USERNAME_FIELD” https://stackoverflow.com/questions/51308530/attributeerror-type-object-myuser-has-no-attribute-username-field/51311357
#   https://stackoverflow.com/questions/51308530/attributeerror-type-object-myuser-has-no-attribute-username-field/51311357
# Custom User Registration Django (AbstractBaseUser and UserCreationForm) : https://www.youtube.com/watch?v=oZUb372g6Do
