from rest_framework import serializers

from .models import Medicine, PurchaseRequest, Demand, User


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['name', 'description', 'price', 'count']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PurchaseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRequest
        fields = ['user', 'medicine_id']


class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = ['user', 'medicines']