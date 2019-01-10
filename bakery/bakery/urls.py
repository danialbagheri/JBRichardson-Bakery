"""bakery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from web.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home),
    url('accounts/login/',
         auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    url('accounts/change-password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html',success_url="/accounts/password_change_done/"), name="change-password"),
    url('accounts/password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name="change-password-done"),
    url('accounts/logout/',
         auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    url(r'^accounts/profile/$', profile, name='profile'),
    url(r'^accounts/order/$', order, name='order')
]
