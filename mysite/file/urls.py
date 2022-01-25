from django.urls import path
from . import views
app_name = 'file'
urlpatterns = [

 path('upload3/', views.upload3, name='upload3'),
]