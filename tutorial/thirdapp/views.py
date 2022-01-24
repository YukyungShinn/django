from django.shortcuts import render
from django.http import HttpResponse
from .models import Shop
from .models import JejuOlle
def shop(request):
    shop_list = Shop.objects.all()
    return render(
    request,
    'thirdapp/shop.html',
    {'shop_list': shop_list}
)

def jeju_olle(request):
    data=JejuOlle.objects.all()
    result=''    
    for d in data:
        result += d.course_name
    return HttpResponse(result)