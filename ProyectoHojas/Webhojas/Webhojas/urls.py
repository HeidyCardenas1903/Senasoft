from django.urls import path
from . import wiews
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('crear-venta/', wiews.crear_venta, name='crear_venta'),
    path('listar-ventas/', wiews.listar_ventas, name='listar_ventas'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('algoritmia.urls')),
]
