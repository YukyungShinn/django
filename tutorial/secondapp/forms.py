from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course

        fields = ['name', 'cnt']  # id 속성은 PK 이므로 사용하지 않음

        labels = {  # 오류 메시지에 보여줄 단어
            'name': '과정명',
            'cnt': '인원수'
    }