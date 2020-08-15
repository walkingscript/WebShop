from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import GoodCategory


def index(request: HttpRequest) -> HttpResponse:
    """View для отображения главной страницы каталога товаров."""

    gc = GoodCategory.objects.all()

    context = {
        'gc': gc
    }
    return render(request, 'catalog/index.html', context)
