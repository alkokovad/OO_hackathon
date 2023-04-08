from django.urls import path

from . import views

urlpatterns = [
    # post views
    path("login/", "django.contrib.auth.views.login", name='login'),
    path('logout/', 'django.contrib.auth.views.logout', name='logout'),
    path('logout-then-login/', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    path('', views.dashboard, name='dashboard'),
]
