from multiprocessing.context import assert_spawning
from django.shortcuts import render
from accounts.models import Profile,Tag

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
        rating=request.POST['rating']
        assignmentsRating=request.POST['AssignmentsRating']
        attendanceRating=request.POST['AttendanceRating']
        clarityRating=request.POST['ClarityRating']
        timingRating=request.POST['TimingRating']
        print(rating)
        print(assignmentsRating)
        print(attendanceRating)
        print(clarityRating)
        print(timingRating)


    return render(request,'profile.html',{'info':info,"tags":tags}) 