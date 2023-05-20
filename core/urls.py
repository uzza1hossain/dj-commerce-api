"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.registration.views import ResendEmailVerificationView
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import LoginView
from dj_rest_auth.views import LogoutView
from dj_rest_auth.views import PasswordChangeView
from dj_rest_auth.views import PasswordResetConfirmView
from dj_rest_auth.views import PasswordResetView
from dj_rest_auth.views import UserDetailsView
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenVerifyView

from users.views import SellerRegistrationAPIView

dj_rest_auth_urls = [
    path(
        "password-reset/confirm/<uidb64>/<token>/",
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name="password_reset_confirm",
    ),
    path(
        "password/reset/", PasswordResetView.as_view(), name="rest_password_reset"
    ),  # OK
    path(
        "password/reset/confirm/",
        PasswordResetConfirmView.as_view(),
        name="rest_password_reset_confirm",
    ),  # OK
    path(
        "signup/seller/",
        SellerRegistrationAPIView.as_view(),
        name="seller-signup",
    ),  # OK. My own custom seller registration view based on RegisterView
    path("signup/user/", RegisterView.as_view(), name="rest_register"),  # OK
    path(
        "signup/email-verify/", VerifyEmailView.as_view(), name="rest_verify_email"
    ),  # OK
    path(
        "signup/email-resend/",
        ResendEmailVerificationView.as_view(),
        name="rest_resend_email",
    ),  # OK
    path("login/", LoginView.as_view(), name="rest_login"),  # OK
    path("logout/", LogoutView.as_view(), name="rest_logout"),  # OK
    path(
        "password/change/", PasswordChangeView.as_view(), name="rest_password_change"
    ),  # OK
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),  # OK
    path("token/refresh/", get_refresh_view().as_view(), name="token_refresh"),  # OK
    # path("me/", UserDetailsView.as_view(), name="rest_user_details"),  # OK
    re_path(
        r"^account-confirm-email/(?P<key>[-:\w]+)/$",
        TemplateView.as_view(),
        name="account_confirm_email",
    ),  # OK
    path(
        "account-email-verification-sent/",
        TemplateView.as_view(),
        name="account_email_verification_sent",
    ),  # OK
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("chaining/", include("smart_selects.urls")),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"
    ),
    path("api/v1/auth/", include(dj_rest_auth_urls)),
    path("api/v1/addresses/", include("address.urls")),
    path("api/v1/categories/", include("categories.urls")),
    path("api/v1/", include("brands.urls")),
    path("api/v1/", include("media_assets.urls")),
]
