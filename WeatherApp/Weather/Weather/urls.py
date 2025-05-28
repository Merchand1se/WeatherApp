from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', include('app.urls')),
    path('', views.Home.as_view(), name='home'),
]
