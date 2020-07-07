from django.contrib import admin

# Register your models here.
# from myproject.myapp.models import Author
from hello.models import Person

class PersonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Person,PersonAdmin)