from django.urls import path
from . import views
app_name='firstapp'
urlpatterns = [
    path('form/model/',views.form_model, name='form_model'),
    path('main/', views.main),
    path('insert/',views.insert),
    path('show/', views.show),
    path('req/get/', views.req_get),
    path('req/post/', views.req_post,
    name='post'),
    path('req/ajax4/', views.req_ajax4),
    path('req/json/', views.req_json),
    path('tag/', views.tag),
    path('filter/', views.filter),
    path('custom_filter/', views.custom_filter),
    path('custom_filter/', views.custom_filter),
    path('template/', views.template),
]