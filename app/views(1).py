from django.shortcuts import render, redirect
from .models import ProductTracker, Product, ShippingInfo
from .forms import SignUpForm, LoginForm, ShippingInfoForm, SupportForm
from django.contrib.auth import login, logout
# Create your views here.

def support_view(request):
    submitted = False

    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = SupportForm()

    return render(request, 'app/support.html', {'form': form, 'submitted': submitted})

def shipping_view(request):
    if request.method == 'POST':
        form = ShippingInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app/shipping_success.html', {'form': form})
    else:
        form = ShippingInfoForm()
    return render(request, 'app/shipping.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'app/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

def Home(request):
    tracking_id = request.GET.get("tracking_id")
    context = {}

    if tracking_id:
        try:
            tracker = ProductTracker.objects.get(tracking_id=tracking_id)
            context["tracker"] = tracker
        except ProductTracker.DoesNotExist:
            context["error"] = "Tracking ID not found. Please check and try again."

    return render(request, "app/index.html", context)


def Tracking(request):
    return render(request, "app/tracking.html")