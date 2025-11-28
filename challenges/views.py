from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
        return HttpResponse(monthly_challenges[month])
    except:
        return HttpResponseNotFound("Not supported!")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(month):
        return HttpResponseNotFound("Not supported!")
    
    target_month = months[month - 1]

    return HttpResponseRedirect('/chall/' + target_month)