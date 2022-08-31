from django.shortcuts import render
from accounts.models import Profile

# Create your views here.
def index(request):
    return render(request,'index.html')

def dept(request,department):
    data=Profile.objects.filter(department=department)
    return render(request,'dept.html',{"data":data,'dept':department})    

def team(request):
    return render(request,'team.html') 

def contact(request):
    return render(request,'contact.html') 
    
def profile(request):
    return render(request,'profile.html') 