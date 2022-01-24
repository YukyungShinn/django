"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path, include
from firstapp import views  # views파일을 불러온다. 어디서? firstapp폴더에서. 
from. import views as config_views # views를 config_views로 부르겠다. 라는 말입니다. 여기서 view는 config폴더에 있는
                                        # view입니다. 왜냐하면 지금 이 파일(urls.py)가 config폴더에 있기 때문입니다!
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index1/', config_views.index1),
    path('index2/', config_views.index2),
    path('home/', config_views.home),
    path('first/', include('firstapp.urls')),
    path('second/',include('secondapp.urls')),
    path('third/', include('thirdapp.urls')),
    path(
        'text/<str:char>/',
        config_views.text
        ),
    path(
        '<int:year>/<int:month>/',
        config_views.date
        ),
    path('search/', config_views.search),
    path('info/', config_views.info),
    path('req/get/', views.req_get),
    path('req/post/', views.req_post),
    path('member/', include('member.urls')),
    path('paging/', include('paging.urls')),
    path('file/', include('file.urls')),
    
]+static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
