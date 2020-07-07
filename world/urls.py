from django.conf.urls import url 
import world.views as wv

urlpatterns = [
    url(r'^/world_models$',wv.show ,name = 'show'),
    url(r'^/models$',wv.show ,name = 'show'),
]