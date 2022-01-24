from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Member
from django.utils import timezone
from django.http import HttpResponse



def signup_custom(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        user_name = request.POST.get('user_name')

        m = Member(
            user_id=user_id, user_pw=user_pw, user_name=user_name)
        m.date_joined = timezone.now()
        m.save()
        return HttpResponse(
        '가입 완료<br>%s %s %s' % (user_id, user_pw, user_name))
    else:
        return render(request, 'member/signup_custom.html')

def login_custom(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        try:
            m = Member.objects.get(user_id=user_id, user_pw=user_pw)
        except Member.DoesNotExist as e:
            return HttpResponse('아이디 또는 비밀번호가 틀렸습니다.')
        else:
            request.session['user_id'] = m.user_id
            request.session['user_name'] = m.user_name
        # 회원정보 조회 실패 시 예외 발생
        return redirect('member:login')
    else:
        return render(request, 'member/login_custom.html')

def logout_custom(request):
    del request.session['user_id'] # 개별 삭제
    del request.session['user_name'] # 개별 삭제
    request.session.flush() # 전체 삭제
    return redirect('member:login')