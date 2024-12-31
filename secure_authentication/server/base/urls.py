
from django.urls import path
from . import views
from .views import CustomTokenObtainPairView, CustomTokenRefreshView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.logout, name="logout"),
    path('register/', views.reqister, name="register"),
    path('is_authenticated/', views.is_authenticated, name="is_authenticated"),
    path('notes/', views.getNotes, name="notes"),
]