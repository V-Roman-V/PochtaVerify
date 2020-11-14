from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Package

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_packs = Package.objects.all().count()
    num_packs_ready=Package.objects.filter(status='r').count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_packs': num_packs, 'num_packs_ready': num_packs_ready},
    )