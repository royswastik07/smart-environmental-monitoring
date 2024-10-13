from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Landing Page
    path('index/', views.index, name='index'),  # Index Page
    path('air/', views.air_view, name="air"),
    path('noise/', views.noise_view, name="noise"),
    path('data.html', views.data_view, name='data'),
    path('aboutus/', views.about_us, name='aboutus'),
    path('login/', views.login_view, name='login'),  # Updated path for combined login and register
    path('logout/', views.logout_view, name='logout'),  # Logout path
]
