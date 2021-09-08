from django.urls import path, re_path
from api import views
from .views import clients, products, Bill, saveclients


urlpatterns = [
    #path('client/', views.clientApi),
    #path('client/file', views.saveClients),
    #path('client/product', views.productApi)

    path('client/', clients.as_view(), name='client_list'),
    path('products/', products.as_view(), name='product_list'),
    path('bills/', Bill.as_view(), name='bill_list'),
    path('save/', saveclients.as_view(), name='save_list')
]