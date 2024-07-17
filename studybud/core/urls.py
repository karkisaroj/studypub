from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('screen/<str:pk>/',views.screen,name='screen'),
]