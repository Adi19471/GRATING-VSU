from django.shortcuts import render,redirect

from .forms import UserReg
# Create your views here.

def home(request):
    return render(request, 'dtl/home.html')

def about(request):
    return render(request, 'dtl/about.html')

def contact(request):
    return render(request, 'dtl/contact.html')



def college(request):
    return render(request, 'dtl/college.html')

def gallery(request):
    return render(request, 'dtl/gallery.html')

# def login(request):
#     return render(request, 'dtl/login.html')

def register(request):
    form = UserReg()
    if request.method == 'POST':
        form = UserReg(request.POST)
        if form.is_valid():

            form.save()
            return redirect('login')
    form = UserReg()
            
    return render(request, 'dtl/register.html',{'form':form})


    