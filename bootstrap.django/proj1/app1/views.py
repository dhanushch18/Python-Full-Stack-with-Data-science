from django.shortcuts import render

from.models import card


# Create your views here.

def fun(request):
    dict_card={
        'img':card.objects.all()
    }
    return render(request,'boot.html',dict_card)
