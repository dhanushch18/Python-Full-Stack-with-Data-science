from django.shortcuts import render

from.models import card


# Create your views here.
def fun(request):
    dict_card={
        'img':card.objects.all()
    }
    return render(request,'boot2.html',dict_card)
