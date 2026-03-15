from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('yoga/', views.yoga, name='yoga'),
    path('meditation/', views.meditation, name='meditation'),
    path('festival/', views.festival, name='festival'),
    path('agriculture/', views.agriculture, name='agriculture'),
    path('food/', views.food, name='food'),

    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change-password/', views.change_password, name='change_password'),
    path('profile/activity/', views.view_activity, name='view_activity'),

    path('yoga/', views.yoga, name='yoga'),
    path('yoga/surya-namaskar/', views.surya_detail, name='surya_detail'),
    

]
