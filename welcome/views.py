import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

# Create your views here.

# render(request, template, dict) - returns an HttpResponse object w/ result of rendered template

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())

def linked_pages(request, page):  # parses requests -> links
    print("called linked pages view...")
    print("Requested Page: {}".format(page))
    return render(request, 'welcome/{}'.format(page))