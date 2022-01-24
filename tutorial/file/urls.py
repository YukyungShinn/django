from django.urls import path
from . import views
app_name = 'file'

urlpatterns = [
    path('upload1/', views.upload1, name='upload1'),
    path('upload2/', views.upload2, name='upload2'),
    path('upload3/', views.upload3, name='upload3'),
    path('download/', views.download, name='download'),
    path('img_show/', views.img_show, name='img_show'),
]