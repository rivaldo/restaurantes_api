from rest_framework import generics, viewsets, filters
from restaurantes.models import Restaurante, Prato
from restaurantes.serializers import RestauranteSerializer, PratoSerializer, ListaPratosDeUmRestauranteSerializer
from django_filters.rest_framework import DjangoFilterBackend

class RestauranteViewSet(viewsets.ModelViewSet):
    """Recurso de restaurantes"""
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    http_method_names = ['get', 'post']
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']

class PratoViewSet(viewsets.ModelViewSet):
    """Recurso de pratos de um restaurante"""
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer
    http_method_names = ['get', 'post']
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']

class ListaPratosDeUmRestauranteView(generics.ListAPIView):
    """Listando pratos de um restaurante"""
    def get_queryset(self):
        queryset = Prato.objects.filter(restaurante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaPratosDeUmRestauranteSerializer