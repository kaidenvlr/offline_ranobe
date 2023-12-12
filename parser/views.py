from django.http import HttpResponseRedirect
from django.shortcuts import render

from parser.forms import SearchForm
from parser.models import Ranobe


def home(request):
    if request.method == 'POST':
        url = request.POST['url']
        

