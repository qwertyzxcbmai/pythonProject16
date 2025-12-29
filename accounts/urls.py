from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('admin-register/', views.admin_register_view, name='admin_register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
