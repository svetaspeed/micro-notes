from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'announce', 'full_text', 'date']

        widgets = {

            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'article title'
            }),

            "announce": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'announcement'
            }),

            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'date'
            }),

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'text'
            }),

        }