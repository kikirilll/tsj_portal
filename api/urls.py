from django.urls import path, include
from rest_framework import routers
from . import views


# router = routers.SimpleRouter()
router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', views.login, name='login'),
    path('test_token/', views.test_token, name='test_token'),
    path('profiles/counters/', views.profile_counters, name='profile_counters'),
    path('profiles/counters/add/', views.add_counter, name='add_counter'),
]