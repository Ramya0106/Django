from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse

from .models import Person


def somefunction(request):
    return HttpResponse("Hello app. You're at the polls index.")

def get_all_person(request):
    data = Person.objects.all()
    print(data)
    post_list = serializers.serialize('json', data)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")