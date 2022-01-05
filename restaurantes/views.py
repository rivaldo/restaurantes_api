from django.http.response import JsonResponse
from drf_yasg.openapi import Response
from rest_framework import generics, viewsets, filters
from rest_framework.views import APIView
from restaurantes.models import Restaurante, Prato
from restaurantes.serializers import RestauranteSerializer, PratoSerializer, ListaPratosDeUmRestauranteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status

class RestauranteViewSet(viewsets.ModelViewSet):
    """Recurso de restaurantes"""
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    http_method_names = ['get', 'post', 'put', 'path', 'delete']
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']

class PratoViewSet(viewsets.ModelViewSet):
    """Recurso de pratos de um restaurante"""
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer
    http_method_names = ['get', 'post', 'put', 'path', 'delete']
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    filterset_fields = ['tag']

class ListaPratosDeUmRestauranteView(generics.ListAPIView):
    """Listando pratos de um restaurante"""
    def get_queryset(self):
        queryset = Prato.objects.filter(restaurante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaPratosDeUmRestauranteSerializer

class ListandoTagsView(APIView):
    def get(self, request):
        tags = {
        "tags": [
            {
            "value": "Italiana",
            "color": "green"
            },
            {
            "value": "Japonesa",
            "color": "red"
            },
            {
            "value": "Doces",
            "color": "blue"
            },
            {
            "value": "Diet",
            "color": "yellow"
            },
            {
            "value": "Massas",
            "color": "indigo"
            },
            {
            "value": "Caldos",
            "color": "orange"
            },
            {
            "value": "Light",
            "color": "cyan"
            },
            {
            "value": "Vegetariana",
            "color": "sky"
            },
            {
            "value": "Mexicana",
            "color": "fuchsia"
            },
            {
            "value": "Francesa",
            "color": "pink"
            },
            {
            "value": "Espanhola",
            "color": "rose"
            },
            {
            "value": "Mineira",
            "color": "teal"
            },
            {
            "value": "Baiana",
            "color": "emerald"
            },
            {
            "value": "Molhos",
            "color": "lime"
            },
            {
            "value": "Saladas",
            "color": "amber"
            },
            {
            "value": "Americana",
            "color": "purple"
            }
        ]
        }
        return JsonResponse(tags, status=status.HTTP_200_OK)