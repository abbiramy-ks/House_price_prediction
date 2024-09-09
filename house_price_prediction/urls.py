from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prediction.urls')),  # Include prediction app's URLs
]
