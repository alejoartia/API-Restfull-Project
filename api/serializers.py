from rest_framework import serializers
from django.db.models import fields
from django.contrib.auth.models import User
from .models import Person, Clients, Products, Bills, BillProducts


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        user = User.objects.filter(username = data)
        if len(user) != 0:
            raise serializers.ValidationError("This user already exist, Introduce a new one")
        else:
            return data


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name',)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('id', 'document', 'first_name', 'last_name', 'email', 'created_on', 'update_at')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'description', 'price', 'stock', 'created_on', 'update_at')


class BillSerializer(serializers.ModelSerializer):
    # client = ClientSerializer(read_only=True)
    class Meta:
        model = Bills
        fields = ('id', 'client_id', 'company_name', 'nit', 'code', 'created_on', 'update_at')


class BillProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillProducts
        fields = ('id', 'bill_id', 'product_id', 'created_on', 'update_at')