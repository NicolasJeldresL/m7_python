from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import indexView

urlpatterns = [
    path('', indexView, name='home'),
     path('login/', auth_views.LoginView.as_view(), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout page
    path('register/', views.register, name='register'),  # Register page (your custom view)
]

