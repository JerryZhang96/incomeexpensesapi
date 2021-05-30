from django.urls import path
from .views import RegisterView, VerifyEmailView, LoginView, PasswordTokenCheckView, RequestPasswordResetEmailView, SetNewPasswordView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('email-verify/', VerifyEmailView.as_view(), name="email-verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('reset-email/', RequestPasswordResetEmailView.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckView.as_view(), name="password-reset-confirm"),
    path('password-reset-complete', SetNewPasswordView.as_view(),
         name="password-reset-complete")

]
