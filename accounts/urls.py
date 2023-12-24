
from django.urls import path
from . import views
urlpatterns = [
    path('',views.profile,name='profile'),
    path('register/', views.register, name='register'),
    path('dashboard/',views.home,name='home'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
]