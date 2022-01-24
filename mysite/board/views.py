from django.shortcuts import render,get_object_or_404,redirect
from .models import Review,Answer
from django.utils import timezone
from .forms import ReviewForm,AnswerForm
from django.http import HttpResponse
from django.core.paginator import Paginator  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def index(request):
    #board의 목록 출력
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어    # 페이징처리
    review_list = Review.objects.order_by('-create_date')
    if kw:
        review_list = review_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw)  # 내용검색
            #Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            #Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    paginator = Paginator(review_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'review_list': page_obj,'page': page, 'kw': kw}
    return render(request, 'board/review_list.html', context)

def detail(request, review_id):
    #board의 내용 출력
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'board/review_detail.html', context)

def review_create(request):
    #board의 질문 등록
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.create_date = timezone.now()
            review.save()
            return redirect('board:index')
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'board/review_form.html', context)

def answer_create(request, review_id):
    # board의 댓글 등록
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.review = review
            answer.save()
            return redirect('board:detail', review_id=review.id)
    else:
        form = AnswerForm()
    context = {'review': review, 'form': form}
    return render(request, 'board/review_detail.html', context)  

@login_required(login_url='common:login')
def review_modify(request, review_id):
    #pybo 질문수정
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('board:detail', review_id=review.id)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.modify_date = timezone.now()  # 수정일시 저장
            review.save()
            return redirect('board:detail', review_id=review.id)
    else:
        form = ReviewForm(instance=review)
    context = {'form': form}
    return render(request, 'board/review_form.html', context)

@login_required(login_url='common:login')
def review_delete(request, review_id):
    #board 질문삭제
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('board:detail', review_id=review.id)
    review.delete()
    return redirect('pybo:index')

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    #board 답변수정
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('board:detail', answer_id=answer.review.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('board:detail', review_id=answer.review.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'board/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    #board 답변삭제
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('board:detail', review_id=answer.review.id)


