# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.views import LoginView
# import logging
# # 配置日志记录器
# logger = logging.getLogger(__name__)
# # learning_notes/learning_notes/users/views.py
#
# class CustomLoginView(LoginView):
#     template_name = 'users/login.html'
#     def form_valid(self, form):
#         # 获取用户名和密码
#         # username = form.cleaned_data.get('username')
#         # password = form.cleaned_data.get('password')
#         # # 输出用户名、密码和验证结果
#         # print(f"用户名: {username}")
#         # print(f"密码: {password}")
#         # print("验证结果: 成功")
#         # return super().form_valid(form)
#
#         # 获取用户名和密码
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         # 输出用户名、密码和验证结果
#         print(f"用户名: {username}")
#         print(f"密码: {password}")
#         print("验证结果: 成功")
#
#         # 调用 super().form_valid(form) 前输出日志
#         logger.info("准备调用 super().form_valid(form)")
#         try:
#             response = super().form_valid(form)
#             # 调用成功后输出日志
#             logger.info("super().form_valid(form) 调用成功")
#             return response
#         except Exception as e:
#             # 捕获异常并输出错误信息
#             logger.error(f"super().form_valid(form) 调用失败: {str(e)}")
#             raise
#
#     def form_invalid(self, form):
#         # 获取用户名和密码
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         # 输出用户名、密码和验证结果
#         print(f"用户名: {username}")
#         print(f"密码: {password}")
#         print("验证结果: 失败")
#         print(form.errors)  # 打印表单错误信息
#         return super().form_invalid(form)
#
# def register(request):
#     """注册新用户"""
#     if request.method != 'POST':
#         # 显示空的注册表单
#         form = UserCreationForm()
#     else:
#         # 处理填写好的表单
#         form = UserCreationForm(data=request.POST)
#
#         if form.is_valid():
#             new_user = form.save()
#             # 让用户自动登录，再重定向到主页
#             login(request, new_user)
#             return redirect('learning_logs:index')
#
#     # 显示空表单或指出表单无效
#     context = {'form': form}
#     return render(request, 'users/register.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse  # 导入 reverse 函数

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def form_valid(self, form):
        # 获取用户名和密码
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        # 输出用户名、密码和验证结果
        print(f"用户名: {username}")
        print(f"密码: {password}")
        print("验证结果: 成功")
        return super().form_valid(form)

    def form_invalid(self, form):
        # 获取用户名和密码
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        # 输出用户名、密码和验证结果
        print(f"用户名: {username}")
        print(f"密码: {password}")
        print("验证结果: 失败")
        print(form.errors)  # 打印表单错误信息
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('learning_logs:topics')# 重定向到 index 页面

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向到主页
            login(request, new_user)
            return redirect('learning_logs:index')

    # 显示空表单或指出表单无效
    context = {'form': form}
    return render(request, 'users/register.html', context)