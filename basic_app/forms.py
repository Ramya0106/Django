from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name must be start with z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Enter your email again:")
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False,
                                widget = forms.HiddenInput,
                                validators = [validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super(FormName,self).clean()
        email = all_clean_data.get('email')
        verify_email = all_clean_data.get('verify_email')
        if email != verify_email:
            raise forms.ValidationError("Make Sure Emails Match")
        return all_clean_data

        