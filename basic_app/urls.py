from django.conf.urls import url
import basic_app.views as ba

app_name = 'basic_app'

urlpatterns = [
    url(r'^index$',ba.index,name='index'),
    url(r'^formPage',ba.form_name_view,name='form_name_view'),
    url(r'^base',ba.basic,name = 'basic'),
    url(r'other',ba.other,name = 'other'),
]