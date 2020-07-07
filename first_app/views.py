from django.shortcuts import render
from django.http import HttpResponse
from hello.models import Person
from django.core import serializers

# Create your views here.
def index(request):
    main_data = {}
    data = Person.objects.all()
    args = {
        'data':data
    }
    return render(request,'first_app/index.html',args)
