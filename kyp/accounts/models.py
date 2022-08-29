from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=30)
    department=models.CharField(max_length=10)
    rating=models.FloatField(null=True,blank=True,default=None)
    post=models.CharField(max_length=20)
    pic=models.ImageField()
    email=models.EmailField()
    ph_num=models.IntegerField(max_length=12,null=True)
    
    def __str__(self):
        return self.name