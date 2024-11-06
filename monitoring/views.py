from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages 
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import CustomUser

@login_required
def user_management(request):
    users = CustomUser.objects.all()
    context = {'users': users}
    return render(request, 'monitoring/user_management.html', context)

@login_required
def admin_dashboard(request):
    # Existing stats
    total_users = CustomUser.objects.count()
    new_signups = CustomUser.objects.filter(date_joined__gte=timezone.now() - timezone.timedelta(days=7)).count()
    active_sessions = CustomUser.objects.filter(last_login__gte=timezone.now() - timezone.timedelta(days=1)).count()

    # Get all users for User Management section
    users = CustomUser.objects.all()

    context = {
        'total_users': total_users,
        'new_signups': new_signups,
        'active_sessions': active_sessions,
        'recent_activities': CustomUser.objects.order_by('-last_login')[:5],
        'users': users,
    }

    return render(request, 'monitoring/admin_dashboard.html', context)

@login_required
def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        
        if username and email and phone_number:
            new_user = CustomUser.objects.create(
                username=username,
                email=email,
                phone_number=phone_number
            )
            new_user.set_password('default_password')  # Optionally set a default password
            new_user.save()
            messages.success(request, 'New user added successfully.')
        else:
            messages.error(request, 'Please fill out all fields.')
        return redirect('user_management')


@login_required
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('admin_dashboard')



@login_required
def profile_view(request):
    return render(request, 'monitoring/profile.html', {'user': request.user})


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