from unittest import result
from django.shortcuts import redirect, render
from django.http import HttpResponse

from secondapp.forms import CourseForm

def main(request):
    return HttpResponse('<u>Main</u>')

from .models import ArmyShop, Course
def insert(request):
    Course.objects.create(name='데이터 분석',cnt=30)
    c = Course(name='데이터 수집',cnt=20)
    c.save()
    Course(name='웹개발',cnt=25).save()
    Course(name='인공지능',cnt=20).save()
    return HttpResponse('데이터 입력 완료')

def show(request):
    c=Course.objects.all()
    # result= ''
    # for a in c:
    #     result+='%s %s<br>'%(a.name,a.cnt)#포매팅 사용
        
    # return HttpResponse(result)

    return render(
        request,'secondapp/show.html',
        {'data': c }
    )


def armyshop(request):
    shop=ArmyShop.objects.all()
    return render(
        request, 
        'secondapp/army_shop.html',
        {'data': shop }
    )

def armyshop2(request,year,month):
    shop=ArmyShop.objects.filter(year=year, month=month)
    #result=''
    #for i in shop:
    #    result+='%s %s %s<br>' %(i.year, i.month, i.name)

    result=['%s %s %s<br>' % (i.year, i.month, i.name) for i in shop]

    return HttpResponse(''.join(result))

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.forms.models import model_to_dict
@csrf_exempt
def ajaxGet(request):

    #QuerySet []
    c=Course.objects.all()
    
    data=[]
    #model_to_dict - 조회된 데이터를 dict 형태로 변경
    for a in c:
        d=model_to_dict
        data.append(d)


    return JsonResponse(data,safe=False)

def ajaxExam(request):
    
    return render(request, 'second/ajax_exam.html')
from django.shortcuts import redirect
from secondapp.forms import CourseForm
def course_create(request):
    if request.method == 'POST':
        # 1. 입력된 데이터를 한꺼번에 저장
        # 2. 유효성 검사 결과가 저장
        form=CourseForm( request.POST )
        if form.is_valid():
            #데이터 저장
            # course=form.save(commit=False)
            # course.save()
            form.save()
            #어딘가로 이동, 메세지 출력, ...
            # return redirect('firstapp:post')
            return redirect('secondapp:course_create')
    else:
        form = CourseForm()
        

    return render(request, 'secondapp/course_create.html',{'form':form})