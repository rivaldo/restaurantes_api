from rest_framework import serializers
from restaurantes.models import Restaurante, Prato

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'

class PratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prato
        fields = '__all__'