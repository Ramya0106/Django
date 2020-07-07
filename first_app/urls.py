from django.conf.urls import url
import first_app.views as fa

urlpatterns = [
    url(r'^/click',fa.index,name='index'),
    url(r'^/hover',fa.index,name='index'),
    url(r'^/clickHOVER',fa.index,name='index'),
]