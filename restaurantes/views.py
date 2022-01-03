from rest_framework import viewsets, filters
from restaurantes.models import Restaurante, Prato
from restaurantes.serializers import RestauranteSerializer, PratoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    http_method_names = ['get', 'post']
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']

class PratoViewSet(viewsets.ModelViewSet):
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer
    http_method_names = ['get', 'post']
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']