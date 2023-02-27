from django.http import HttpResponse
from .models import *
from django.shortcuts import render


def main_landing(request):
    arguments = {
        'title': 'records',
        'page_title':  'Database Content',
        'records': Product.objects.all()
    }
    return render(request, 'landing/draft.html', arguments)
