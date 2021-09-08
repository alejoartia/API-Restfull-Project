from django.contrib import admin
from .models import Person, Clients, Products, Bills, BillProducts

admin.site.register(Person)
admin.site.register(Clients)
admin.site.register(Products)
admin.site.register(Bills)
#admin.site.register(BillProducts)
