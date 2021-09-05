from django.shortcuts import render, reverse
from datetime import datetime
import os


def get_pages():
    pages = {'Главная страница': reverse('home'),
             'Показать текущее время': reverse('time'),
             'Показать содержимое рабочей директории': reverse('workdir')
             }
    return pages


def home_view(request):
    template_name = 'app/home.html'
    context = {'title': 'Выберите раздел',
               'pages': get_pages()
               }
    return render(request, template_name, context)


def time_view(request):
    template_name = 'app/home.html'
    current_time = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
    context = {'title': 'Текущее дата и время',
               'pages': get_pages(),
               'content': [current_time]
               }
    return render(request, template_name, context)


def workdir_view(request):
    template_name = 'app/home.html'
    directories_file = os.listdir()
    dir_list = directories_file

    context = {'title': 'Список файлов в рабочей директории:',
               'pages': get_pages(),
               'content': dir_list
               }

    return render(request, template_name, context)
