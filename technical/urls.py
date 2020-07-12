from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('phone/', views.phone,name='phone'),
    path('products/<int:myid>', views.productView, name="ProductView"),
    path('tv/', views.tv,name='tv'),
    path('laptop/', views.laptop,name='laptop'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)