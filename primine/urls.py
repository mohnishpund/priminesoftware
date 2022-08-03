from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('sign/', include('sign.urls')),
    path('sign/', include('django.contrib.auth.urls')),
]
