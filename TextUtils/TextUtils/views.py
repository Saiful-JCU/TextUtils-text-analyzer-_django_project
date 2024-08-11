# this file created by saiful islam

from django.http import HttpResponse
from django.shortcuts import render
import re # for capitalyze function

def index(request):

    return render(request, 'index.html')

def index2(request):

    return render(request, 'index2.html')

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    fullcap = request.GET.get('fullcap','off')
    removespace = request.GET.get('removespace','off')
    wordcount = request.GET.get('wordcount','off')
    vowelcount = request.GET.get('vowelcount','off')
    charcount = request.GET.get('charcount','off')
    removepunc=request.GET.get('removepunc','off')
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
        
    
    elif charcount == 'on':
        count = 0
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEGHIJKLMNOPQRSTUVWXYZ' 
        for char in djtext:
            if char in characters:  # Check if the character is a vowel
                count += 1

        text = f'Your text has {count} charecters.'
        params = {'purpose': 'Count Charecters', 'analyzed_text': text}
        return render(request, 'analyze.html', params)

    elif vowelcount == 'on':
        count = 0
        vowels = 'aeiouAEIOU'
        for vowel in djtext:
            if vowel in vowels:
                count += 1
        text = f'Your text has {count} vowels.'
        params = {'purpose': 'Count Vowels', 'analyzed_text': text}
        return render(request, 'analyze.html', params)
    
    elif wordcount == 'on':
        words = djtext.split()
        count = len(words)
        text = f'Your text has {count} words.'
        params = {'purpose': 'Count Words', 'analyzed_text': text}
        return render(request, 'analyze.html', params)

    elif removespace == 'on':
        ls = djtext.split()
        sentence  = ' '.join(ls)
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': sentence}
        return render(request, 'analyze.html', params)
    
    elif fullcap == 'on':
        analyzed = ""       
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Capitalize First Characters of word', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')

    

    
