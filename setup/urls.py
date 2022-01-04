from django.contrib import admin
from django.urls import path, include
from restaurantes.views import RestauranteViewSet, PratoViewSet, ListaPratosDeUmRestauranteView
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="API de restaurantes e pratos",
      default_version='v1',
      description="Provedor local de restaurantes e pratos desenvolvida pela Alura para o curso de React",
      terms_of_service="#",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('restaurantes', RestauranteViewSet, basename='Restaurantes')
router.register('pratos', PratoViewSet, basename='Pratos')

urlpatterns = [
    path('admin-api/', admin.site.urls),
    path('api/', include(router.urls) ),
    path('api/restaurantes/<int:pk>/pratos/', ListaPratosDeUmRestauranteView.as_view() ),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
