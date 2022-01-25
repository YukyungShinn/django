from django.urls import path
from . import views
from .views import * 

app_name='board'

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:review_id>/',views.detail,name='detail'),
    path('comment/create/<int:review_id>/',
        views.comment_create,name='comment_create'),
    path('review/create/', views.review_create, name='review_create'),
    path('review/modify/<int:review_id>/', 
        views.review_modify, name='review_modify'),
    path('review/delete/<int:review_id>/', 
        views.review_delete, name='review_delete'),
    path('comment/modify/<int:comment_id>/', 
        views.comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>/',
        views.comment_delete, name='comment_delete'),
]