from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.allStudent, name='home'),
    path('pdf/<int:pk>/', views.pdf, name='pdf'),
    path('pdf-test/', views.pdfTest, name='pdf-test'),

    path('range/<int:start>/<int:end>/', views.queryRange, name='range'),
    path('qr/', views.qr, name='qr'),
]
