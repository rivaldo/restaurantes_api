from django.http.response import JsonResponse
from drf_yasg.openapi import Response
from rest_framework import generics, viewsets, filters
from rest_framework.views import APIView
from restaurantes.models import Restaurante, Prato
from restaurantes.serializers import RestauranteSerializer, PratoSerializer, ListaPratosDeUmRestauranteSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class=None

class RestauranteViewSet(viewsets.ModelViewSet):
    """Recurso de restaurantes"""
    permission_classes = (IsAuthenticated,)
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']
    pagination_class=None

class PratoViewSet(viewsets.ModelViewSet):
    """Recurso de pratos de um restaurante"""
    permission_classes = (IsAuthenticated,)
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    filterset_fields = ['tag']
    pagination_class=None

class ListaPratosDeUmRestauranteView(generics.ListAPIView):
    """Listando pratos de um restaurante"""
    def get_queryset(self):
        queryset = Prato.objects.filter(restaurante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaPratosDeUmRestauranteSerializer
    pagination_class=None
    permission_classes = (IsAuthenticated,)

class ListaRestaurantesView(generics.ListAPIView):
    """Listando restaurante"""
    def get_queryset(self):
        queryset = Restaurante.objects.all()
        return queryset
    serializer_class = RestauranteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']

class ListaPratosView(generics.ListAPIView):
    """Listando restaurante"""
    def get_queryset(self):
        queryset = Prato.objects.all()
        return queryset
    serializer_class = PratoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    filterset_fields = ['tag']


class ListandoTagsView(APIView):
    permission_classes = (IsAuthenticated,)
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