from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }  
    context = {'title': 'Выберите раздел',
               'pages': pages
               }
    return render(request, template_name, context)


def time_view(request):
    template_name = 'app/home.html'
    current_time = datetime.now().utcnow()
    msg = {'сейчас': current_time}

    context = {'title': f'Текущее дата и время: {current_time}'}
             

    return render(request, template_name, context)


def workdir_view(request):
    template_name = 'app/home.html'
    directories_file = os.listdir()
    msg = "<br>".join(directories_file)

    context = {'title': 'Список файлов в рабочей директории:',
               'pages': directories_file
               }

    return render(request, template_name, context)
