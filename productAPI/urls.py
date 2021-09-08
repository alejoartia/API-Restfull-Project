"""productAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.api import UserAPI
from api.views import PersonList
from api.views import Login
from api.views import Logout
from rest_framework.authtoken import views
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create_user/1.0/', UserAPI.as_view(), name="api_create_user"),
    path('api/person/2.0/', PersonList.as_view(), name='person_list'),
    path('api_generate_token/', views.obtain_auth_token),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('api/3.0/', include(('api.url', 'api'))),
    path('', include('api.url')),
    #path('admin/', admin.site.urls), url(r'^', include('productAPI.urls'))
]
