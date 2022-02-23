from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import place
from . forms import mform
from . models import cricket

# Create your views here.
# def fun(request):
#     o=cricket.objects.all()
#     ob=place.objects.all()
#     return render(request,"index.html",{'result':ob,'res':o})
     # return render(request,"index.html",{'result':ob})

def fun(request):
    ob1=place.objects.all()
    return render(request,"movie.html" ,{'result':ob1})
def details(request,place_id):
    ob2=place.objects.get(id=place_id)
    return render(request,"details.html",{'re':ob2})
def add(request):
    if(request.method=='POST'):




        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        img=request.FILES['img']
        sav=place(name=name,desc=desc,img=img)
        sav.save()
    return render(request,"add.html")
def edit(request,id):
    mov=place.objects.get(id=id)

    moveform=mform(request.POST or None,request.FILES,instance=mov)
    if moveform.is_valid():
        moveform.save()
        return redirect('/')




    return render(request,'edit.html',{'m':mov,'mmform':moveform})

