from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'aboutus.html')

def products(request):
    return render(request, 'products.html')

def contact(request):
    return render(request, 'contact.html')
