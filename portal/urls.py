from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . forms import ExtendedAuthenticationForm

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='portal/login.html', authentication_form=ExtendedAuthenticationForm)),
    path('logout/', auth_views.LogoutView.as_view()),
    path('buildings/', views.buildings_list, name='buildings_list'),
    path('buildings/create', views.add_building, name='add_building'),
    path('buildings/delete/<int:building_id>/', views.delete_building, name='delete_building'),
    path('buildings/update/<int:building_id>/', views.update_building, name='update_building'),
    path('users/', views.users_list, name='users_list'),
    path('users/create/', views.add_user, name='add_user'),
    path('users/delete/<int:profile_id>/', views.delete_profile, name='delete_profile'),
    path('users/update/<int:profile_id>/', views.update_user, name='update_user'),
    path('users/user-counters/<int:user_profile_id>/', views.profile_counters, name='profile_counters'),
]