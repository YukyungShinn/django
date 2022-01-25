from django import forms
from board.models import Review,Comment
from django import forms
from django.forms import ModelForm, models

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review  # 사용할 모델
        fields = ['subject', 'content','file']  
        # ReviewForm에서 사용할 Review 모델의 속성
        labels = {
            'subject': '제목',
            'content': '내용',
            'file':'이미지',
        } 
    # def __init__(self, *args, **kwargs):
    #     self.fields['file'].required = False ?

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }