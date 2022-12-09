from django.shortcuts import render
from django.http import HttpResponse
from . import utils

def index(request):
    utils.save_screen()
    #return HttpResponse("<img>")
    return render(request, 'showwindow/index.html')

