from django.shortcuts import render
# from hello.models import Person
from form_module.forms import NewUserForm
# Create your views here.
def index(request):
    return render(request,"form_module/index.html")

def person_info(request):
    # main_data = {}
    # data = Person.objects.all()
    # args = {
    #     'data':data
    # }
    # return render(request,'form_module/form_page.html',args)
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("Error Form Invalid")
    return render(request,'form_module/form_page.html',{'form':form})