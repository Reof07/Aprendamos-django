from django.urls import path

from .views import ( home,
    articulos,
    tecnologia,
    tutoriales,
    detallePost
     )

# nombre de espacio.

urlpatterns = [
    path('', home, name = 'index'),
    path('articulos/', articulos, name = 'articulos'),
    path('tecnologia/', tecnologia, name = 'tecnologia'),
    path('tutoriales/', tutoriales, name = 'tutoriales'),
    path('<slug>/', detallePost, name = 'detalle_post'),

]