from django.shortcuts import render, HttpResponse 

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html') 
def scheme1(request):
    return render(request,'scheme1.html') 
def scheme2(request):
    return render(request,'scheme2.html') 
def scheme3(request):
    return render(request,'scheme3.html') 

# Create your views here.
