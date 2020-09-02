from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import GoodCategory


def index(request: HttpRequest) -> HttpResponse:
    """View для отображения главной страницы каталога товаров."""

    categories = GoodCategory.objects.all()

    context = {
        'categories': categories
    }
    return render(request, 'catalog/index.html', context)
