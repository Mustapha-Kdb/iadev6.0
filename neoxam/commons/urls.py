# -*- coding: utf-8 -*-
from django.urls import path, include

from users import views as user_views

urlpatterns = [
    path('',user_views.login_user, name="login"),
    path('sign up/',user_views.register, name ='register'),
]
