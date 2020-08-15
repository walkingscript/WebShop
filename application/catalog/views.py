from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """View для отображения главной страницы каталога товаров."""
    context = {
        'info': 'Hello, World! Привет всем программистам! Аливарыя можа быць и топ, але я люблю Корону.'
    }
    return render(request, 'catalog/index.html', context)
