from django.db import models
import datetime


class Person(models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField('First_name', max_length=100)
    last_name = models.CharField('Last_name',max_length=200)

    def __str__ (self):
        return '{0},{1}'.format(self.last_name,self.first_name)


class Clients(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    document = models.CharField(max_length=50,null=False, unique=True)
    first_name = models.CharField(max_length=200,null=False)
    last_name = models.CharField(max_length=200,null=False)
    email = models.CharField(max_length=255,null=False)
    created_on = models.DateField(null=False, auto_now_add=True)
    update_at = models.DateField(null=False,auto_now_add=True)


class Products(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, null=True)
    price = models.FloatField(default=0.0, null=False)
    stock = models.IntegerField(default=0, null=False)
    created_on = models.DateField( null=False,auto_now_add=True)
    update_at = models.DateField( null=False,auto_now_add=True)


class Bills(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    client_id = models.ForeignKey('Clients', on_delete=models.CASCADE,)
    company_name = models.CharField(max_length=200, null=False)
    nit = models.IntegerField( null=False)
    code = models.CharField(max_length=255,null=False, unique=True)
    created_on = models.DateField(null=False,auto_now_add=True)
    update_at = models.DateField(null=False,auto_now_add=True)


class BillProducts(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey('Bills',on_delete=models.CASCADE,)
    product_id = models.ForeignKey('Products',on_delete=models.CASCADE,)
    created_on = models.DateField( null=False,auto_now_add=True)
    update_at = models.DateField( null=False,auto_now_add=True)