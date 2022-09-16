from asyncio.windows_events import NULL
from multiprocessing.context import assert_spawning
from tkinter import Entry
from django.shortcuts import render
from accounts.models import Profile,Tag,Rate,AvgRating

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
        ratings=[data.assignmentsRating,data.attendanceRating,data.clarityRating,data.timingRating]
        records=Rate.objects.filter(profile_id=pk).count()
        print("records ")
        print(records)
        is_record=True
        try:
            entry=AvgRating.objects.get(profile_id=pk)
            
        except:
            is_record=False

                    
        
        if is_record:
            avgRatings=[entry.avgAssignmentsRating,entry.avgAttendanceRating,entry.avgClarityRating,entry.avgTimingRating]
        else:
            avgRatings=[0,0,0,0]   
        
        
        newAvg=[]
        
        for value,avgOld in zip(ratings,avgRatings):
            avgNew=avgOld+(value-avgOld)/records 
            newAvg.append(round(avgNew,1)) 
             
        avgdata=AvgRating(avgAssignmentsRating=newAvg[0],avgAttendanceRating=newAvg[1],avgClarityRating=newAvg[2],avgTimingRating=newAvg[3],profile_id=pk)

        avgdata.save()
    return render(request,'profile.html',{'info':info,"tags":tags}) 