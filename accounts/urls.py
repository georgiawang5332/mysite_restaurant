from django.urls import path
from . import views
from accounts.views import *
from django.contrib.auth.views import LoginView

# Create your urls here.
app_name = 'accounts'

urlpatterns = [
  path('login/', views.LoginView.as_view(), name='login'),
  # path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
  path('', views.home, name='home'),
]
