from django.contrib import admin

# Register your models here.
from world.models import Topic,Webpage,Access_record

admin.site.register(Access_record)
admin.site.register(Topic)
admin.site.register(Webpage)
