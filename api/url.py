from django.urls import path, re_path
from api import views


urlpatterns = [
    path('client/', views.clientApi),
    path('client/file', views.saveClients),
    path('client/product', views.productApi)

]