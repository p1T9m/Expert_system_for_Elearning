from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_view
from ExpertSystem import views 
from second_expert import views as second

urlpatterns = [
    path('',include('core.urls')),
    path('register/',user_view.register, name='register'),
    path('profile/',user_view.profile, name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html')
         , name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html')
         , name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html')
         , name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html')
         , name='password_reset_complete'),
    path('expert-system/', views.expert_system, name='expert_system'),
    path('beginner-page/', views.beginner_page, name='beginner_page'),
    path('intermediate-page/', views.intermediate_page, name='intermediate_page'),
    path('advanced-page/', views.advanced_page, name='advanced_page'),
    path('second-expert/', second.second_expert, name='second_expert'),
    path('beginner/', second.beginner, name='beginner'),
    path('inter/', second.inter, name='inter'),
    path('advanced/', second.advanced, name='advanced'),
    path("admin/", admin.site.urls, name='admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
