from django.urls import path

from . import views

app_name='board'

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:review_id>/',views.detail,name='detail'),
    path('answer/create/<int:review_id>/',
        views.answer_create,name='answer_create'),
    path('review/create/', views.review_create, name='review_create'),
    path('review/modify/<int:review_id>/', 
        views.review_modify, name='review_modify'),
    path('review/delete/<int:review_id>/', 
        views.review_delete, name='review_delete'),
    path('answer/modify/<int:answer_id>/', 
        views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
        views.answer_delete, name='answer_delete'),
    
    
]