from django.shortcuts import render , redirect
from user_app.forms import CustomRegisterForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
         register_form = CustomRegisterForm(request.POST)
         if register_form.is_valid():
             register_form.save()   
             messages.success(request,'new user  Successfully')
             return redirect('register')
         else:
             messages.success(request,"May Be The User Password Or Name Is Wrong Try Again Please")
             return redirect('register')
    else: 
           register_form = CustomRegisterForm()
           return render(request, 'register.html',{'register_form':register_form})
    