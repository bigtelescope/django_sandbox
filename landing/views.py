from django.http import HttpResponse
from .models import *
from django.shortcuts import render


def main_landing(request):
    arguments = {
        'title': 'records',
        'page_title':  'Records Page Title',
        'records': Product.objects.all()
    }
    return render(request, 'landing/draft.html', arguments)


def sandbox(request):
    return render(request, 'landing/base.html')
