from django.conf.urls import url
from adv_cbv_hello import views

app_name = 'adv_cbv_hello'

urlpatterns = [
    # url(r'^$',views.CBview.as_view(),name = "adv_index"),
    # url(r'^index$', views.IndexView.as_view(), name="adv_index2"),
    url(r'^list',views.SchoolListView.as_view(),name = "list"),
    url(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name = "detail"),
    url(r'^create/$',views.SchoolCreateView.as_view(),name = "create"),
    url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name = "update"),
    url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name="delete"),
]