from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_view
from ExpertSystem import views 


urlpatterns = [
    path('',include('core.urls')),
    path('register/',user_view.register, name='register'),
    path('profile/',user_view.profile, name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('expert-system/', views.expert_system, name='expert_system'),
    path('beginner-page/', views.beginner_page, name='beginner_page'),
    path('intermediate-page/', views.intermediate_page, name='intermediate_page'),
    path('advanced-page/', views.advanced_page, name='advanced_page'),
    path("admin/", admin.site.urls, name='admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
