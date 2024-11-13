from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'groceryapp/index.html')

def about(request):
    return render(request,'groceryapp/about.html')

def access(request):
    return render(request,'groceryapp/access.html')
