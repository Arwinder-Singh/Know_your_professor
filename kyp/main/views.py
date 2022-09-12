from multiprocessing.context import assert_spawning
from django.shortcuts import render
from accounts.models import Profile,Tag,Rate
from .forms import rateForm

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
    
def profile(request,pk):
    info=Profile.objects.filter(id=pk)
    tags=Tag.objects.all()
    for i in info:
        print(i.mainRating)
    if request.method=="POST":
        form=rateForm(request.POST)
        if form.is_valid():
            data=Rate()
            data.assignmentsRating=form.cleaned_data['assignmentsRating']
            data.attendanceRating=form.cleaned_data['attendanceRating']
            data.clarityRating=form.cleaned_data['clarityRating']
            data.timingRating=form.cleaned_data['timingRating']
            data.profile_id=pk
            data.save()
        


    return render(request,'profile.html',{'info':info,"tags":tags}) 