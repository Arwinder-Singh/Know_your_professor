from django.db import models

# Create your models here.
class Tag(models.Model):
        tag_name=models.CharField(max_length=30)
        
        
        def __str__(self):
            return self.tag_name
        
class Profile(models.Model):
    name=models.CharField(max_length=30)
    department=models.CharField(max_length=10)
    mainRating=models.FloatField(null=True,blank=True,default=None)
    post=models.CharField(max_length=20)
    pic=models.ImageField()
    email=models.EmailField()
    ph_num=models.IntegerField(null=True)
    
    
    def __str__(self):
        return self.name
    
class Rate(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='profile')
    assignmentsRating=models.FloatField(null=True,blank=True,default=None)
    attendanceRating=models.FloatField(null=True,blank=True,default=None)
    clarityRating=models.FloatField(null=True,blank=True,default=None)
    timingRating=models.FloatField(null=True,blank=True,default=None)
    
    
    
class AvgRating(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE,related_name='avg_profile',primary_key=True,)
    avgAssignmentsRating=models.FloatField(null=True,blank=True,default=0)
    avgAttendanceRating=models.FloatField(null=True,blank=True,default=0)
    avgClarityRating=models.FloatField(null=True,blank=True,default=0)
    avgTimingRating=models.FloatField(null=True,blank=True,default=0)
    
    

    
    
    
        