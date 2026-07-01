from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from users import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Home
    path("", user_views.home, name="home"),

    # Authentication
    path("login/", user_views.login_view, name="login"),
    path("signup/", user_views.signup_view, name="signup"),
    path("logout/", user_views.logout_view, name="logout"),

    # About
    path("about/", user_views.about_view, name="about"),

    # Disease Detection
    path("upload/", include("disease_detection.urls")),
    path(
    "password-reset/",
    auth_views.PasswordResetView.as_view(
        template_name="password_reset.html"
    ),
    name="password_reset",
),

path(
    "password-reset/done/",
    auth_views.PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"
    ),
    name="password_reset_done",
),

path(
    "reset/<uidb64>/<token>/",
    auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm.html"
    ),
    name="password_reset_confirm",
),

path(
    "reset/done/",
    auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"
    ),
    name="password_reset_complete",
)


]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)