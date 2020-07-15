from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from . import models
# Create your views here.

# def index(request):
#     return render(request,"adv_cbv_hello/index.html")

#for templateview using advance
# class CBview(View):
#     def get(self,request):
#         return HttpResponse("Class based view are cool")
#
# class IndexView(TemplateView):
#     template_name = "adv_cbv_hello/index.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'BASIC INJECTION'
#         return context
class IndexView(TemplateView):
    template_name = 'adv_cbv_hello/index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = "adv_cbv_hello/school_detail.html"