from django import forms
from board.models import Review,Answer


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review  # 사용할 모델
        fields = ['subject', 'content']  
        # ReviewForm에서 사용할 Review 모델의 속성
        labels = {
            'subject': '제목',
            'content': '내용',
        }  

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }