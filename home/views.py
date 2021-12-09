from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
      #  print(name,email,phone,desc)
        ins= Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("The entered data writtten to the database")

    return render(request, 'contact.html')
