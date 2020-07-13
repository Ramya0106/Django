from django.conf.urls import url
import form_module.views as fv

urlpatterns = [
    url(r'^$',fv.index,name='index'),
    url(r'^user',fv.person_info,name="person_info"),
]