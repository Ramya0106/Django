from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
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

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("adv_cbv_hello:list")
