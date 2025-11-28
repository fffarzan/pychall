from django.urls import path
from . import views

urlpatterns = [
    path('<int:month>', views.monthly_challenge_by_number), # order matters
    path('<str:month>', views.monthly_challenge, name='month-chall'),
]