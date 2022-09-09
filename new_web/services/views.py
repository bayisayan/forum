from django.shortcuts import render, HttpResponse
import random


def index(request):
    a = random.randrange(5)
    return render(request, 'index.html', {'b': a})


def page(request, page_num):
    a = random.randrange(5)
    return render(request, 'page.html', {'b': a,
                                         'page_num': page_num})
