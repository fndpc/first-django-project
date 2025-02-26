from django.shortcuts import render, redirect
from . models import News
from . forms import NewsForm
from django.http import HttpResponse

def news_home(request):
    news = News.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            return HttpResponse('<b>ПРОВЕРЬТЕ МЕТОД ПЕРЕДАЧИ ДАННЫХ!<b/>')


    form = NewsForm()
    data = {
        'form': form
    }
    return render(request, 'news/create.html', data)
