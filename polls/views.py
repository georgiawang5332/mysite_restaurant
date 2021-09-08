from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import CreateView

from polls.forms import *
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


# Create your views here.

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


# class polls_create(request):
def polls_create(request):
  template_name = 'polls/polls_form.html'
  if not request.user.is_staff or not request.user.is_superuser:  # 基本用戶權限
    raise Http404
  # if not request.user.is_authenticated():
  #   raise Http404

  form = StoreForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    instance = form.save(commit=False)
    print(form.cleaned_data)
    # Store.objects.create(**form.cleaned_data)  # 新增
    instance.save()

    # message success
    messages.success(request, "Successfully Created")
    return HttpResponseRedirect(instance.get_absolute_url())
  else:
    messages.error(request, "Not successfully Created")
  context = {
    'form': form,
  }
  return render(request, template_name, context)


def polls_detail(request, id):
  instance = get_object_or_404(Store, id=id)
  # try:
  #   instance = get_object_or_404(Store, id=id)
  # except Store.DoesNotExist:
  #   raise Http404("Given query not found....Store does not exist")

  context = {
    'instance': instance,
    'title': 'Detail',
  }
  return render(request, 'polls/polls_detail.html', context)


def polls_list(request):  # , id
  # instance = get_object_or_404(Store, id=id)
  queryset_list = Store.objects.all()# .order_by('-id')
  # queryset_list = Store.objects.active()  # .order_by('-id')
  if request.user.is_staff or request.user.is_superuser:
    queryset_list = Store.objects.all()  # .order_by('-id')

  # search
  query = request.GET.get("q")
  if query:
    queryset_list = queryset_list.filter(
      Q(store_name__icontains=query) |
      Q(store_holder__icontains=query) |
      Q(store_phoneNumber__icontains=query) |
      Q(store_address__icontains=query) |
      Q(store_email__icontains=query) |
      Q(store_notes__icontains=query)
    ).distinct()

  # paginator
  paginator = Paginator(queryset_list, 25)  # Show 25 contacts per page.
  page_request_var = 'page'
  page_number = request.GET.get(page_request_var)

  try:
    queryset = paginator.page(page_number)
  except PageNotAnInteger:
    # if page is not an integer, deliver first page.
    queryset = paginator.page(1)
  except EmptyPage:
    queryset = paginator.page(paginator.num_pages)

  page_obj = paginator.get_page(page_number)

  context = {
    'page_request_var': page_request_var,
    'page_obj': page_obj,
    'queryset_list': queryset,
    'title': 'List',
  }
  return render(request, 'polls/polls_list.html', context)
  # return HttpResponse('<h1>List</h1>')


def polls_edit(request, id=None):
  # basic use permissions 基本使用權限
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404

  instance = get_object_or_404(Store, id=id)
  form = StoreForm(request.POST or None, request.FILES or None, instance=instance)

  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    # message success
    messages.success(request, "Successfully Save <a href='#'>ITEM </a> Saved", extra_tags='html_safe')
    return HttpResponseRedirect(instance.get_absolute_url())
  else:
    messages.error(request, "Not successfully Created")
  context = {
    'title': 'edit',
    'instance': instance,
    'form': form,
  }
  return render(request, 'polls/polls_form.html', context)


def polls_delete(request, id=None):
  instance = get_object_or_404(Store, id=id)
  instance.delete()
  messages.success(request, "Successfully delete")
  return redirect('polls:polls_list')


def polls_profile(request):
  context = {
    'title': 'profile',
  }
  return render(request, 'polls/profile.html', context)

  # ////////////////////////////////


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
  templates_name = 'polls/starter.html'
  context = {
    'title': 'test index',
  }
  return render(request, templates_name, context)
