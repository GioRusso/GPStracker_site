from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name = 'home'),
    url(r'^historial$', views.Historial, name = 'historial'),
    url(r'^fecha', views.Fechas, name = 'fechas'),
    url(r'^real_time', views.TiempoReal, name = 'real_time'),
    url(r'^update', views.Update, name = 'update'),
    url(r'^historial_area$', views.Historial_by_area, name = 'historial_by_area'),
    url(r'^areaquery', views.Area, name = 'area'),
]