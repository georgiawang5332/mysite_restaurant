from django.shortcuts import render, redirect
# from django.http import HttpResponse

# from django.contrib.auth import login, authenticate
from polls.forms import RegistrationForm, EditForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

# from django.http import response  # 註冊方法 可刪除
# from polls.forms import RegistrationForm
# from polls.models import *
# from django.contrib.auth.models import User

# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required
def changePassword(request):
  if request.method == "POST":
    form = PasswordChangeForm(data=request.POST, user=request.user)
    if form.is_valid():
      form.save()
      return redirect('polls:polls_profile')
  else:
    form = PasswordChangeForm(user=request.user)
    context = {
      'form': form,
    }
    return render(request, 'polls/change_password.html', context)


def polls_profile_edit(request):
  if request.method == "POST":
    form = EditForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect('polls:polls_detail')
  else:
    form = EditForm(instance=request.user)
    context = {
      'title': 'test index',
      'form': form,
    }
    return render(request, 'polls/polls_edit.html', context)


def polls_delete(request):
  context = {
    'title': 'test index',

  }
  return render(request, 'polls/polls_delete.html', context)


def polls_edit(request):
  if request.method == "POST":
    form = EditForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect('polls:polls_detail')
  else:
    form = EditForm(instance=request.user)
    context = {
      'title': 'test index',
      'form': form,
    }
    return render(request, 'polls/polls_edit.html', context)


def polls_detail(request):
  context = {
    'title': 'test index',

  }
  return render(request, 'polls/polls_detail.html', context)


def polls_create(request, ):
  context = {
    'title': 'test index',

  }
  return render(request, 'polls/polls_create.html', context)


def polls_list(request):
  context = {
    'title': 'test index',
    'user': request.user,
  }
  return render(request, 'polls/polls_list.html', context)


def polls_profile(request):
  context = {
    'title': 'profile',
  }
  return render(request, 'polls/profile.html', context)

  # ////////////////////////////////////


def contact(request):
  context = {
    'title': 'test index',
  }
  return render(request, 'basic_company_info/contact.html', context)


@login_required
def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
      form.save()
    return redirect('/polls')
  else:
    form = RegistrationForm()
    context = {
      'form': form,
    }
    return render(request, 'registration/reg_form.html', context)

  # two method crispy_form
  # def register(request):
  #   if response.method == 'POST':
  #     form = RegistrationForm
  #     if form.is_valid():
  #       form.save()
  #     return redirect("/polls")
  #   else:
  #     form = RegistrationForm()
  #
  #   context = {
  #     'form': form,
  #   }
  #
  #   return render(response, 'registration/reg_form.html', context)

  # one method
  # def registration_view(request):
  #   context = {}
  #   if request.POST:
  #     form = RegistrationForm(request.POST)
  #     if form.is_valid():
  #       form.save()
  #       email = form.cleaned_data.get('email')
  #       raw_pw = form.cleaned_data.get('pw1')
  #       account = authenticate(email=email, password=raw_pw)
  #       login(request, account)
  #       return redirect('/polls')
  #     else:
  #       context['registration_form'] = form
  #   else:  # GET request
  #     form = RegistrationForm()
  #     context['registration_form'] = form
  #   return render(request, 'registration/reg_form.html', context)

@login_required
def starter(request):
  context = {
    'title': 'test index',
  }
  return render(request, 'polls/starter.html', context)
