from django.conf.urls import url
from learning_user import views
app_name = 'learning_user'

urlpatterns = [
    url(r'^register/$',views.register,name = 'register'),
]