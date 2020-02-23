from django.shortcuts import render , redirect
from .models import pasterDB
# Create your views here.


def index(request):
    return render(request,"index.html")

def paster(request):
    data_paste=None
    if request.method == "POST":
        paste1 = request.POST.get('textpaste','')
        name = request.POST.get('pastename','')
        user = pasterDB(textss_field=paste1,namess=name)
        user.save()
        data_paste = pasterDB.objects.get(namess=name)
    #return redirect('paster',name=name)
    return render(request,"paste.html",{'data_paste':data_paste})



def view(request,name):
    data_paste = pasterDB.objects.get(namess=name)
    return render(request,"paste.html",{'data_paste':data_paste})
