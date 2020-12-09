from django.urls import path

from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('demo', views.demo, name='demo'),
    path('/', views.demo, name='demo')
]