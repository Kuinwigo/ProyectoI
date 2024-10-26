# encuesta/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('survey/', views.survey_form, name='survey_form'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Redirige al login después de cerrar sesión
]
