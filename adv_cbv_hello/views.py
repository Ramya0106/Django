from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return render(request,"adv_cbv_hello/index.html")

class CBview(View):
    def get(self,request):
        return HttpResponse("Class based view are cool")

class IndexView(TemplateView):
    template_name = "adv_cbv_hello/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'
        return context