# this file created by saiful islam

from django.http import HttpResponse
from django.shortcuts import render
import re # for capitalyze function

def index(request):

    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # CHECK CHECKBOX VALUES
    fullcap = request.POST.get('fullcap','off')
    removespace = request.POST.get('removespace','off')
    wordcount = request.POST.get('wordcount','off')
    vowelcount = request.POST.get('vowelcount','off')
    charcount = request.POST.get('charcount','off')
    removepunc=request.POST.get('removepunc','off')
    removenumber = request.POST.get('removenum', 'off')
    
    # CHECK WHICH CHECKBOX IS ON
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        
    if charcount == 'on':
        count = 0
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEGHIJKLMNOPQRSTUVWXYZ' 
        for char in djtext:
            if char in characters:  # Check if the character is a vowel
                count += 1

        text = f'Your text has {count} charecters.'
        params = {'purpose': 'Count Charecters', 'analyzed_text': text}
        

    if vowelcount == 'on':
        count = 0
        vowels = 'aeiouAEIOU'
        for vowel in djtext:
            if vowel in vowels:
                count += 1
        text = f'Your text has {count} vowels.'
        params = {'purpose': 'Count Vowels', 'analyzed_text': text}
        return render(request, 'analyze.html', params)
    
    if wordcount == 'on':
        words = djtext.split()
        count = len(words)
        text = f'Your text has {count} words.'
        params = {'purpose': 'Count Words', 'analyzed_text': text}
        return render(request, 'analyze.html', params)

    if removespace == 'on':
        ls = djtext.split()
        sentence  = ' '.join(ls)
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': sentence}
        djtext = sentence
    
    if fullcap == 'on':
        analyzed = ""       
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Capitalize All Characters of text', 'analyzed_text': analyzed}
        djtext = analyzed

    if removenumber == 'on':
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Numbers ', 'analyzed_text': analyzed}
        djtext = analyzed
          
    if (removepunc != 'on' and removenumber != 'on' and removespace !='on' and fullcap != 'on' and wordcount != 'on' and charcount != 'on' and wordcount != 'on' and vowelcount != 'on'):
        return HttpResponse("Please select any operation and try again!")

    return render(request, 'analyze.html', params)
    

    

    
