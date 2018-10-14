import os
import django

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    return render(request, 'hello/index.html', {'hostname': hostname })


    