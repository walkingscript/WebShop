import pytz
import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """View для отображения главной страницы каталога товаров."""
    context = {
        'info': 'Just a test: ' +
                str(datetime.datetime.now(pytz.timezone('Europe/Minsk')).
                    strftime("%d %B %Y %H:%M:%S")),
    }
    return render(request, 'catalog/index.html', context)
