"""Afisha1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from movie_app.views import *
from User.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/test/', ),
    path('api/v1/movie/', MovieModelViewSet),
    path('api/v1/director/', DirectorModelViewSet.as_view()),
    path('api/v1/review/', ReviewModelViewSet.as_view()),
    path('api/v1/movies/ <int:id>/',MovieModelViewSet.as_view()),
    path('api/v1/director/ <int:id>/',DirectorModelViewSet.as_view()),
    path('api/v1/review/ <int:id>/',ReviewModelViewSet.as_view()),
    path('api/v1/users/authorization/', AuthorizationCreateAPIView.as_view()),
    path('api/v1/users/registration/', RegistrationCreateAPIView.as_view()),




]
