from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from world.models import Topic,Webpage,Access_record


def show(request):
    webpage_list = Access_record.objects.order_by('date')
    date_dict = {'access_record':webpage_list}
    return render(request,'world/index.html',context = date_dict)