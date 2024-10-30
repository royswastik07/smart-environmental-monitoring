from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages 
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'monitoring/profile.html', {'user': request.user})

def admin_dashboard(request):
    return render(request, 'monitoring/admin_dashboard.html')

@login_required
def room1(request):
    return render(request, 'monitoring/room/room1.html')

@login_required
def room2(request):
    return render(request, 'monitoring/room/room2.html')

@login_required
def room3(request):
    return render(request, 'monitoring/room/room3.html')

@login_required
def room4(request):
    return render(request, 'monitoring/room/room4.html')

@login_required
def room5(request):
    return render(request, 'monitoring/room/room5.html')

# Air View
def air_view(request):
    location = "Your Area"
    aqi = 45
    aqi_condition = "Good"
    temperature = 22

    context = {
        'location': location,
        'aqi': aqi,
        'aqi_condition': aqi_condition,
        'temperature': temperature,
    }

    return render(request, 'monitoring/air.html', context)

# Noise View
def noise_view(request):
    location = "Your Area"
    noise_level = 55  # Example noise level in dB
    noise_condition = "Moderate"

    context = {
        'location': location,
        'noise_level': noise_level,
        'noise_condition': noise_condition,
    }

    return render(request, 'monitoring/noise.html', context)

# Data View
def data_view(request):
    return render(request, 'monitoring/data.html')

# About Us View
def about_us(request):
    return render(request, 'monitoring/aboutus.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('landing_page')  # Redirect to landing page after logout


# Landing Page View
def landing_page(request):
    return render(request, 'monitoring/landing.html')  # Render the landing page

# Index Page View (for logged-in users)
@login_required
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if user is not authenticated
    return render(request, 'monitoring/index.html')


# Authentication View (Register and Login)
def login_view(request):
    if request.method == 'POST':
        if 'register' in request.POST:  # Check if the registration form is submitted
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                messages.success(request, 'Registration successful! Please log in.')
                return redirect('login')
            else:
                messages.error(request, 'Registration failed. Please check your details.')

        elif 'login' in request.POST:  # Check if the login form is submitted
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(username=username, password=password)
                if user is not None:
                    # Check if user is admin (superuser) or has the specific username
                    if user.is_superuser or user.username == 'swastik_r2002':
                        login(request, user)
                        return redirect('admin_dashboard')  # Redirect to admin dashboard
                    else:
                        # Regular user login
                        login(request, user)
                        return redirect('index')  # Redirect to index for regular users
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid login credentials.")
    else:
        form = CustomUserCreationForm()  # Initialize the registration form

    return render(request, 'monitoring/login.html', {'form': form})