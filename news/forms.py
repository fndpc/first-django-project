from . models import News
from django.forms import ModelForm, widgets

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'full_text', 'url']
        widgets = {
            'title': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'full_text': widgets.Textarea(attrs={'class': 'form-control', 'rows': 15, 'placeholder': 'Введите текст новости'}),
            'url': widgets.URLInput(attrs={'class': 'form-control', 'placeholder': 'Введите URL'}),
        }
        



