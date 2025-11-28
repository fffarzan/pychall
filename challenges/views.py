from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    'jan': 'snowww',
    'feb': 'more snowwww',
    'mar': 'less sowm',
    'apr': 'raaaiin',
    'may': 'more raaiiin',
    'jun': 'little rain',
    'jul': 'sunnnnn',
    'aug': 'super sun',
    'sep': 'softer sun',
    'oct': 'leaffffs',
    'nov': 'many leafss',
    'dec': 'no leaf, near snowww' 
}

def monthly_challenge(request, month):
    try:
        return HttpResponse(f'<h1>{monthly_challenges[month]}</h1>')
    except:
        return HttpResponseNotFound('<h1>Not supported!</h1>')

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(month):
        return HttpResponseNotFound('<h1>Not supported!</h1>')
    
    target_month = months[month - 1]
    redirect_path = reverse('month-chall', args=[target_month]) # result: /chall/jan

    return HttpResponseRedirect(redirect_path)