from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('', views.index, name='index'),
]
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]