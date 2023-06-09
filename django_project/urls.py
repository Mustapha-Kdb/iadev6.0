"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')) """

from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from neoxam.factory_app import views as factory_views
admin.autodiscover()
from django.contrib import admin

admin.site.site_header = 'GpTools Administration'                    # default: "Django Administration"




urlpatterns = [
    path('admin/', admin.site.urls),
#partie urls de users 
    path('login/',user_views.login_user, name="login"),
    path('logout/',user_views.logout_user, name="logout"),
    path('sign up/',user_views.register, name ='register'),
    path('profile/',user_views.profile, name ='profile'),

    path('',user_views.login_user, name="login"),
    path('',include('django.contrib.auth.urls')),
    
    path('GPtools/', factory_views.handle_home, name='factory-home'),

    path('GPtools/', include('neoxam.urls')),
    path('Gpcommons/', include('neoxam.commons.urls')),
    
    
    
    

]
     