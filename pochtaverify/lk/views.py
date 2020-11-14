from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Package
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import PackageForm # новый

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

class HomePageView(ListView):
    model = Package
    template_name = 'home.html'

class CreatePackageView(CreateView): # новый
    model = Package
    form_class = PackageForm
    template_name = 'package.html'
    success_url = reverse_lazy('home')