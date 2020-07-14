from django.conf.urls import url
from adv_cbv_hello import views

app_name = 'adv_cbv_hello'

urlpatterns = [
    url(r'^$',views.CBview.as_view(),name = "adv_index"),
    url(r'^index$', views.IndexView.as_view(), name="adv_index2")
]