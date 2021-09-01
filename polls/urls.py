from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
  # path('home/', views.home, name='home'),  添加額外 請觀看42 新頁面
  # path('login/', views.login, name='login'),
  # path('logout/', views.logout, name='logout'),

  path('profile/', views.polls_profile, name='polls_profile'),  # http://127.0.0.1:8000/posts/list
  path('edit/', views.polls_profile_edit, name='polls_profile_edit'),  # http://127.0.0.1:8000/posts/3/edit/
  path('changePassword/', views.changePassword, name='changePassword'),  # http://127.0.0.1:8000/posts/3/edit/

  # CURD
  path('<int:id>/detail/', views.polls_detail, name='polls_detail'),  # http://127.0.0.1:8000/posts/9/
  path('create/', views.polls_create, name='polls_create'),  # http://127.0.0.1:8000/posts/create
  path('list/', views.polls_list, name='polls_list'),  # http://127.0.0.1:8000/posts/list
  path('<int:id>/edit/', views.polls_edit, name='polls_edit'),  # http://127.0.0.1:8000/posts/3/edit/
  # path('<int:id>/delete/', views.polls_delete, name='polls_delete'),  # http://127.0.0.1:8000/posts/delete
  path('delete/', views.polls_delete, name='polls_delete'),  # http://127.0.0.1:8000/posts/delete

  # 其他畫面
  path('contact/', views.contact, name='contact'),
  # path('', views.login_redirect, name='login_redirect'),
  # path('register/', views.registration_view, name='register'),
  path('register/', views.register, name='register'),
  path('', views.starter, name='starter'),





  path('login/', auth_view.LoginView.as_view(template_name='registration/login.html'), name='login'),
  path('logout/', auth_view.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),

  # 密碼改變
  path('password_change/', auth_view.PasswordChangeView.as_view(), name='password_change'),
  # 密碼改變成功
  path('password_change/done/', auth_view.PasswordChangeDoneView.as_view(), name='password_change_done'),

# '''
# 1 - Submit email form                      //PasswordResetView.as_view()              提交電子郵件表格
# 2 - Email sent success message             //PasswordResetDoneView.as_view()          郵件發送成功信息
# 3 - Link to password Reset Form in email   //PasswordResetConfirmView.as_view()       鏈接到電子郵件中的密碼重置表格
# 4 - Password successfully changed message  //PasswordResetCompleteView.as_view()      密碼更改成功消息
# '''

  # 忘記密碼 重設密碼
  path('password_reset/', auth_view.PasswordResetView.as_view(), name='password_reset'),
  # 忘記密碼 重設密碼 成功
  path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(), name='password_reset_done'),
  #
  path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
  # 密碼已更改
  path('reset/done/', auth_view.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
  # 密碼寄件
  # path('reset_password_sent/', auth_view.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
# Create your urls here.
app_name = 'polls'

