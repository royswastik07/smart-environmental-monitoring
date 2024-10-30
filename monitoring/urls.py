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
    path('profile/', views.profile_view, name='profile'),
    path('room1/', views.room1, name='room1'),
    path('room2/', views.room2, name='room2'),
    path('room3/', views.room3, name='room3'),
    path('room4/', views.room4, name='room4'),
    path('room5/', views.room5, name='room5'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
