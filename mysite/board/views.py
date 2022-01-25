from django.shortcuts import render,get_object_or_404,redirect
from .models import Review,Comment
from django.utils import timezone
from .forms import ReviewForm,CommentForm
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
            #Q(comment__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    paginator = Paginator(review_list, 15)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'review_list': page_obj,'page': page, 'kw': kw}
    return render(request, 'board/review_list.html', context)

def detail(request, review_id):
    #board의 내용 출력
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'board/review_detail.html', context)



def review_create(request):
    #board의 질문 등록(사진 업로드 가능하게 못했음)
    if request.method == 'POST':
        form = ReviewForm(request.POST,request.FILES)
        subject=request.POST['subject']
        content=request.POST['content']
        file=request.POST['file']
        if form.is_valid():
            review = form.save(commit=False)
            name=review.file.name
            size=review.file.size
            review.create_date = timezone.now()
            review.save()
            return redirect('board:index')
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'board/review_form.html', context)

def comment_create(request, review_id):
    # board의 댓글 등록
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now()
            comment.review = review
            comment.save()
            return redirect('board:detail', review_id=review.id)
    else:
        form = CommentForm()
    context = {'review': review, 'form': form}
    return render(request, 'board/review_detail.html', context)  

@login_required(login_url='common:login')
def review_modify(request, review_id):
    #board 질문수정
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
    return redirect('board:index')

@login_required(login_url='common:login')
def comment_modify(request, comment_id):
    #board 답변수정
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('board:detail', comment_id=comment.review.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('board:detail', review_id=comment.review.id)
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'board/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    #board 답변삭제
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect('board:detail', review_id=comment.review.id)

