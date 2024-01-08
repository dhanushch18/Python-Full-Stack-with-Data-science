from django.http import HttpResponse
from django.shortcuts import render

from.forms import bookForm
from.models import book


# Create your views here.
def home(request):
    return HttpResponse("SUCCESSFUL")
def upload1(request):
    form=bookForm
    if request.method=="POST":
        form=bookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return home(request)

    return render(request,'upload1.html',{'form':form})
def upload(request):
    k=book.objects.all()
    return render(request,'upload.html',{'s':k})
def delete_book(request,pk):
    b=book.objects.get(pk=pk)
    b.delete()
    return upload(request)
def view_book(request,pk):
    b=book.objects.get(pk=pk)
    context={
        'instance':b,
        'title':'View Book'
    }

    return render(request,'book.html',context)
def edit_book(request,pk):
    view=book.objects.get(pk=pk)
    form=bookForm(instance=view)
    if request.method=="POST":
        form=bookForm(request.POST,request.FILES,instance=view)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,'upload1.html',{'form':form})
