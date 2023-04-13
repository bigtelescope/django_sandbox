from django.http import HttpResponse
from .models import *
from django.shortcuts import render, get_object_or_404


def main_landing(request):
    arguments = {
        'title': 'records',
        'page_title':  'Database Content',
        'records': Product.objects.all()
    }
    return render(request, 'landing/draft.html', arguments)


def show_record(request, slud_id):
    record = get_object_or_404(Product, slug=slud_id)

    context = {
        'record': record,
        'title': record.title,
        'page_title': record.title
    }

    return render(request, 'landing/base.html', context=context)



def sandbox(request):
    return render(request, 'landing/base.html')


