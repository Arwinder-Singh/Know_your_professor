from django.contrib import admin
from .models import Profile,Tag,Rating,AvgRating
# Register your models here.

admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Rating)
admin.site.register(AvgRating)
