"""KUMAPproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from KUMAPapp import views


if settings.DEBUG:
    urlpatterns = [
        path('index', views.index, name="index"),
        path('', views.first, name="first"),
        path('category/<int:kind>', views.category, name="category"),
        path('detail_ajax/<int:pk>',views.detail_ajax, name="detail_ajax"),
        path('search/', views.search, name='search'),
        path('facility/<int:building_pk>', views.facility, name="facility"),
        path('time/<str:from_building>/<str:to_building>/', views.time, name='time'),
        path('entrance/<int:building_pk>', views.entrance, name="entrance"),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
