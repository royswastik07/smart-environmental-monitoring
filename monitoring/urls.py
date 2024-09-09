from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('air/', views.air_view, name="air"),
    path('noise/', views.noise_view, name="noise"),
    path('data.html', views.data_view, name='data'),
    path('aboutus/', views.about_us, name='aboutus'),

]
