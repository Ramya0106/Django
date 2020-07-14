from django.conf.urls import url
import first_app.views as fa

app_name = 'first_app'

urlpatterns = [
    url(r'^click',fa.index,name='index'),
    url(r'^other',fa.other,name='other'),
    url(r'^relative',fa.relative,name='relative'),
]