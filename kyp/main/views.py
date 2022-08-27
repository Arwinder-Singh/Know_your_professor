from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def dept(request):
    return render(request,'dept.html')    