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
    path('api/v1/movie/', movies_view),
    path('api/v1/director/', movies_view),
    path('api/v1/review/', movies_view),
    path('api/v1/movies/ <int:id>/',movie_detail_view),
    path('api/v1/director/ <int:id>/',director_detail_view),
    path('api/v1/review/ <int:id>/',review_detail_view)
    path('api/v1/users/registration/', registration_view),
    path('api/v1/users/authorization/', authorization_view),
    # # path('api/v1/categories/', Categ.as_view()),
    # # path('api/v1/categories/<int:pk>/', views.CategoryDetailAPIView.as_view()),
    # path('api/v1/tags/', TagmodelViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('api/v1/tags/<int:pk>/', TagmodelViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'partial_update', 'put': 'update', 'delete': 'destroy'})),



]
