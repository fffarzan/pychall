from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
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
    'dec': None,
}

def index(request):
    return render(request, 'challenges/index.html', {
        'months': list(monthly_challenges.keys())
    })

def monthly_challenge(request, month):
    try:
        return render(request, 'challenges/challenge.html', {
            'month': month,
            'text': monthly_challenges[month]
        })
    except:
        raise Http404()

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        raise Http404()
    
    target_month = months[month - 1]
    redirect_path = reverse('month-chall', args=[target_month]) # result: /chall/jan

    return HttpResponseRedirect(redirect_path)