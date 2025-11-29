from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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

def index(request):
    month_list = ''
    months = list(monthly_challenges.keys())

    for m in months:
        cap_month = m.capitalize()
        path = reverse('month-chall', args=[m])
        month_list += f'<li><a href="{path}">{cap_month}</a></li>'

    res = f'<ul>{month_list}</ul>'

    return HttpResponse(res)

def monthly_challenge(request, month):
    try:
        return render(request, 'challenges/challenge.html', {
            'month': month.capitalize(),
            'text': monthly_challenges[month]
        })
    except:
        return HttpResponseNotFound('<h1>Not supported!</h1>')

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('<h1>Not supported!</h1>')
    
    target_month = months[month - 1]
    redirect_path = reverse('month-chall', args=[target_month]) # result: /chall/jan

    return HttpResponseRedirect(redirect_path)