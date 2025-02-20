from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

# app_name = 'users'
# urlpatterns = [
#     # 登录页面
#     path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
#     # 注销页面
#     path('logout/', LogoutView.as_view(), name='logout'),
#     # 注册页面
#     path('register/', views.register, name='register'),
# ]
# from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView
# from . import views

app_name = 'users'
urlpatterns = [
    # 登录页面
    path('login/', views.CustomLoginView.as_view(), name='login'),  # 确保这里使用了正确的视图
    # 注销页面
    path('logout/', LogoutView.as_view(), name='logout'),
    # 注册页面
    path('register/', views.register, name='register'),
]