from django.urls import path
from .views import Home, Tracking, signup_view, login_view, logout_view, shipping_view, support_view

urlpatterns = [
    path('', Home, name="home"),
    path('tracking/', Tracking, name="tracking"),
    path('shipping/', shipping_view, name='shipping'),
    path('support/', support_view, name='support'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]