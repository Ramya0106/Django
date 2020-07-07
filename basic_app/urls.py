from django.conf.urls import url
import basic_app.views as ba

urlpatterns = [
    url(r'^$',ba.index,name='index'),
    url(r'^/formPage',ba.form_name_view,name='form_name_view'),
]