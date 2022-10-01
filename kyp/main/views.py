from asyncio.windows_events import NULL
from multiprocessing.context import assert_spawning
from tkinter import Entry
from django.shortcuts import render,redirect
from accounts.models import Profile,Tag,Rate,AvgRating

from django.http import JsonResponse
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
def temp(request):
    if request.method=="POST":
        name=request.POST.get("product")
        info=Profile.objects.filter(name=name)
        tags=Tag.objects.all()
        for i in info:
            profileID=i.id     
        avgTags=list(AvgRating.objects.filter(profile_id=profileID).values_list('avgAssignmentsRating','avgAttendanceRating','avgClarityRating','avgTimingRating'))
        colTags= list(zip(*avgTags))
        tagInfo=zip(tags,colTags)

        return redirect('profile',pk=profileID)    
    
    
        
       
    return render(request,"search.html")
    
def profile(request,pk):
    info=Profile.objects.filter(id=pk)
    tags=Tag.objects.all()


    avgTags=list(AvgRating.objects.filter(profile_id=pk).values_list('avgAssignmentsRating','avgAttendanceRating','avgClarityRating','avgTimingRating'))
    colTags= list(zip(*avgTags))
    tagInfo=zip(tags,colTags)
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
        
        avg_mainRating=sum(newAvg)/4;
        profile=Profile.objects.get(id=pk)
        profile.mainRating=round(avg_mainRating,1)
        profile.save()
             
        avgdata=AvgRating(avgAssignmentsRating=newAvg[0],avgAttendanceRating=newAvg[1],avgClarityRating=newAvg[2],avgTimingRating=newAvg[3],profile_id=pk)

        avgdata.save()
        
    return render(request,'profile.html',{'info':info,"tags":tags,"tagInfo":tagInfo}) 

def get_names(request):
    payload=list()
    if "term" in request.GET:
        objs=Profile.objects.filter(name__icontains=request.GET.get('term'))
        for obj in objs:
             payload.append(obj.name)
    # name=request.GET.get('name')
    # payload=[]
    # if name:
    #    objs=Profile.objects.filter(name__icontains=name)
    #    for obj in objs:
    #        payload.append(obj.name)
    
    return  JsonResponse(payload,safe=False)      
 


   