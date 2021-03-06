from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home,name='match-home'),
    path('register/', user_views.login, name='match-register'),
    path('profile/', user_views.profile, name='match-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='match-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='match/logout.html'), name='match-logout'),

    # URLS required for Password Reset using Email
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset-done',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
