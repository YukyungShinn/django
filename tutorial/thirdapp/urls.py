from thirdapp import models
from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop),
    path('jeju_olle/',views.jeju_olle),
]