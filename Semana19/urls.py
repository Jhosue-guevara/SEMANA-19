"""
URL configuration for Semana19 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from App1 import views as apv1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',apv1.index,name="home"),
    path('registro/', apv1.reg_user, name='registro'),
    path('login/',apv1.iniciar_sesion,name="login"),
    path('logout/',apv1.cerrar_sesion,name="logout"),
     path('proveedores/agregar/', apv1.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/lista/', apv1.lista_proveedores, name='lista_proveedores'),
    path('proveedores/editar/<int:proveedor_id>/', apv1.editar_proveedor, name='editar_proveedor'),
     path('proveedores/eliminar/<int:proveedor_id>/', apv1.eliminar_proveedor, name='eliminar_proveedor'),
      path('productos/', apv1.lista_productos, name='lista_productos'),
    path('productos/agregar/', apv1.agregar_producto, name='agregar_producto'),
    path('productos/editar/<int:producto_id>/', apv1.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:producto_id>/', apv1.eliminar_producto, name='eliminar_producto'),


    ]
