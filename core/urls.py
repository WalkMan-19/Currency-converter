from django.urls import path
from core import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token-refresh'),

    path('signup', views.SignupView.as_view(), name='signup-view'),
    path('login', views.LoginView.as_view(), name='login-view'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile-view'),
    path('profile/<int:pk>/update_password/', views.UpdatePasswordView.as_view(), name='update_password-view'),
]
