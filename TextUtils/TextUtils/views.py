# this file created by saiful islam

from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

def remove_punc(request):

    return HttpResponse("<h1> removepunc </h1>")
def newline_remove(request):

    return HttpResponse("<h1> New line remover Page </h1>")
def cap_first(request):

    return HttpResponse("<h1> Capitalize first wor. </h1>")

def space_remove(request):

    return HttpResponse("<h1> Extra Space remover page. </h1>")

def char_count(request):

    return HttpResponse("<h1> Character count Page. </h1>")