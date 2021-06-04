from django.shortcuts import render,redirect
from django.http import HttpResponse
from Form_app.models import Register

# message alert form
from django.contrib import messages

# Create your views here.
from Form_app.forms import RegisterForm


def data(request):
    if request.method =='POST':
        f=RegisterForm(request.POST)
        if f.is_valid():
            f.save()
            
        return redirect('data')
    f=RegisterForm()
    return render(request, 'form/data.html',{'form':f})

def display(request):
    messages.info(request,"successfuly  You are Entering The Register Page")
            
    data = Register.objects.all()
    return render(request, 'form/display.html',{'data':data})


def Update(request,id):
    up = Register.objects.get(id=id)
    if request.method == 'POST':
        form = RegisterForm(request.POST,instance=up)
        if form.is_valid():
            form.save()
        return redirect('display')
    form = RegisterForm(instance=up)
    return render(request, 'form/Updatepage.html',{'form':form,'up':up})

def Delete(request,id):
    dl = Register.objects.get(id=id)
    if request.method == 'POST':
        dl.delete()
        return redirect("display")
    return render(request, 'form/Deletepage.html',{'dl':dl})