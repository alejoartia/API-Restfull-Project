from django.shortcuts import render
from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from .models import Clients, Products, Bills, BillProducts
from .serializers import ClientSerializer, ProductSerializer, BillSerializer, BillProductSerializer
import csv
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
#import pandas as pd
import json

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = _url = reverse_lazy('person_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, *kwargs)

    def form_valid(self,form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user=user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)


class Logout(APIView):

    def get(self, request, *args, **kwargs):

        request.user.auth_token.delete()
        logout(request)
        return Response({'result: YOU ARE LOGGED OUT': True})
        #return Response({'result:YOU ARE LOGGED OUT': False})


# Create your views here.
class clients(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    @api_view(['GET','POST'])
    def clientApi(request, id=0):
        if request.method == 'GET':
            clients = Clients.objects.all()
            clients_serializer = ClientSerializer(clients, many=True)
            return JsonResponse(clients_serializer.data, safe=False)

        elif request.method == 'POST':
            clients_data = JSONParser().parse(request)
            clients_serializer = ClientSerializer(data=clients_data, many=True)
            if clients_serializer.is_valid():
                clients_serializer.save()
            return JsonResponse("Added successfully", safe=False)

        elif request.method == 'PUT':
            clients_data = JSONParser().parse(request)
            clients = Clients.objects.get(id=clients_data['id'])
            clients_serializer = ClientSerializer(clients, data=clients_data)
            if clients_serializer.is_valid():
                clients_serializer.save()
                return JsonResponse("Updated successfully", safe=False)
            return JsonResponse("Failed to Update")

        elif request.method == 'DELETE':
            clients = Clients.objects.get(id=id)
            clients.delete()
            return JsonResponse("Delete successfully", safe=False)


class products(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    @api_view(['GET','POST'])
    def productApi(request, id=0):
        if request.method == 'GET':
            products = Products.objects.all()
            products_serializer = ProductSerializer(products, many=True)
            return JsonResponse(products_serializer.data, safe=False)

        elif request.method == 'POST':
            products_data = JSONParser().parse(request)
            products_serializer = ProductSerializer(data=products_data, many=True)
            if products_serializer.is_valid():
                products_serializer.save()
                return JsonResponse("Added successfully", safe=False)
            return JsonResponse("Failed to Add", safe=False)

        elif request.method == 'PUT':
            products_data = JSONParser().parse(request)
            products = Products.objects.get(id=products_data['id'])
            products_serializer = ProductSerializer(products, data=products_data)
            if products_serializer.is_valid():
                products_serializer.save()
                return JsonResponse("Updated successfully", safe=False)
            return JsonResponse("Failed to Update")

        elif request.method == 'DELETE':
            products = Products.objects.get(id=id)
            products.delete()
            return JsonResponse("Delete successfully", safe=False)


class Bill(generics.ListCreateAPIView):
    queryset = Bills.objects.all()
    serializer_class = BillSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    @api_view(['GET','POST'])
    def BIllApi(request, id=0):
        if request.method == 'GET':
            bills = Bills.objects.all()
            bills_serializer = BillSerializer(bills, many=True)
            return JsonResponse(bills_serializer.data, safe=False)

        elif request.method == 'POST':
            bills_data = JSONParser().parse(request)
            bills_serializer = BillSerializer(data=bills_data, many=True)
            if bills_serializer.is_valid():
                bills_serializer.save()
                return JsonResponse("Added successfully", safe=False)
            return JsonResponse("Failed to Add", safe=False)

        elif request.method == 'PUT':
            bills_data = JSONParser().parse(request)
            bills = Bills.objects.get(id=bills_data['id'])
            bills_serializer = ProductSerializer(bills, data=bills_data)
            if bills_serializer.is_valid():
                bills_serializer.save()
                return JsonResponse("Updated successfully", safe=False)
            return JsonResponse("Failed to Update")

        elif request.method == 'DELETE':
            bills = Bills.objects.get(id=id)
            bills.delete()
            return JsonResponse("Delete successfully", safe=False)


class saveclients(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    @api_view(['GET','POST'])
    def saveClients(request):
        file = request.FILES['clients']
        request.readFile(file)
        return JsonResponse('test', safe=False)


    def readFile(file):
        results = []
        with open(str(file)) as File:
            reader = csv.DictReader(File)
            for row in reader:
                results.append(row)
            print(results)
            print(json.dumps(results))
