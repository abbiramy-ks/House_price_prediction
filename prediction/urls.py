from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_price, name='home'),
    path('admin-login/', views.custom_login, name='admin-login'),
]
