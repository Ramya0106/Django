from django import forms
from hello.models import Person
# from django.forms import ModelForm


class NewUserForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

