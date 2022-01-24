from django.shortcuts import render
from secondapp.models import ArmyShop
from django.core.paginator import Paginator
from django.http import HttpResponse

def army_shop(request):
    now_page = request.GET.get('page', 1)

    datas = ArmyShop.objects.order_by('-id')
    p = Paginator(datas, 10)
    now_page=int(now_page)
    info = p.page(now_page)
    info = p.get_page(now_page)
    start_page = (now_page - 1) // 10 * 10 + 1
    end_page = start_page + 9

    context = {
        'info' : info,
        'page_range' : range(start_page, end_page + 1)}
    return render(request, 'paging/army_shop.html', context)

def api(request):
    result = ''
    data = ['a', 'b', 'c', 'd', 'e']
    p = Paginator(data, 3)
    info = p.page(1) # 또는 p.get_page(1)
    result += '전체 데이터 정보 - %s<br>' % data
    result += '전체 데이터 수 - %s<br>' % p.count
    result += '전체 페이지 수 - %s<hr>' % p.num_pages
    result += '1 페이지 데이터 - %s<hr>' % info.object_list
    result += '현재 페이지 데이터 시작번호 - %s<br>' % info.start_index()
    result += '현재 페이지 데이터 종료번호 - %s<hr>' % info.end_index()
    result += '이전 페이지 존재유무 - %s<br>' % info.has_previous()
    if info.has_previous():
        result += '이전 페이지 번호 - %s<br>' % info.previous_page_number()
        result += '다음 페이지 존재유무 - %s<br>' % info.has_next()
    if info.has_next():
        result += '다음 페이지 번호 - %s<br><hr>' % info.next_page_number()
    info = p.page(2)
    result += '2 페이지 데이터 - %s<hr>' % info.object_list
    result += '현재 페이지 데이터 시작번호 - %s<br>' % info.start_index()
    result += '현재 페이지 데이터 종료번호 - %s<hr>' % info.end_index()
    result += '이전 페이지 존재유무 - %s<br>' % info.has_previous()
    if info.has_previous():
        result += '이전 페이지 번호 - %s<br>' % info.previous_page_number()
        result += '다음 페이지 존재유무 - %s<br>' % info.has_next()
    if info.has_next():
        result += '다음 페이지 번호 - %s<br>' % info.next_page_number()
    return HttpResponse(result)