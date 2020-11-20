from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('evaluate_peers/', views.cargar_respuesta, name='cargar_datos'),
    path('view_ratings_par_2/', views.resumen_calificaciones_1, name='resumen_calificaciones_1'),
    path('view_ratings_par_3/', views.resumen_calificaciones_2, name='resumen_calificaciones_2'),
]