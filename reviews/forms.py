from django import forms
from .models import Review
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'movie_name', 'grade']
        
        labels = {
            'title' : '리뷰 제목',
            'content' : '리뷰 내용',
            'movie_name' : '영화 제목',
            'grade' : '영화 평점'
        }