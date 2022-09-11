from django.db import models

# Create your models here.
class Tag(models.Model):
        tag_name=models.CharField(max_length=30)
        
        
        def __str__(self):
            return self.tag_name
        
class Profile(models.Model):
    name=models.CharField(max_length=30)
    department=models.CharField(max_length=10)
    rating=models.FloatField(null=True,blank=True,default=None)
    post=models.CharField(max_length=20)
    pic=models.ImageField()
    email=models.EmailField()
    ph_num=models.IntegerField(null=True)
    tag=models.ManyToManyField(Tag,through="AvgRating")
    
    def __str__(self):
        return self.name
    
class Rating(models.Model):
    R_tag=models.ForeignKey(Tag,on_delete=models.CASCADE,related_name='tag')
    R_profile=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='profile')
    tag_rating=models.FloatField(null=True,blank=True,default=None)
    
class AvgRating(models.Model):
    Avg_tag=models.ForeignKey(Tag,on_delete=models.CASCADE,related_name='avg_tag')
    Avg_profile=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='avg_profile')
    tag_avgRating=models.FloatField(null=True,blank=True,default=None)
    
    class Meta:
        unique_together=[['Avg_tag','Avg_profile']]
    
    
    
        