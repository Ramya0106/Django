"""testsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url

import hello.views as helloV
import world.views 
# import first_app.views as fa
from django.conf.urls import url,include
from django.contrib import admin
from learning_user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', helloV.somefunction),
    path('getpersons/',helloV.get_all_person),
    # path('world/',world.views.show),
    url("world",include('world.urls')),
    url("First_app",include('first_app.urls')),
    url("basic_app",include('basic_app.urls')),
    url("form_module",include('form_module.urls')),
    url(r'^index$',views.index,name = 'index'),
    url(r'^learning_user/',include('learning_user.urls')),
    url(r'^logout/$',views.user_logout,name = 'logout'),
    url(r'special/',views.special,name = 'special'),
    url(r'^adv_cbv_hello',include('adv_cbv_hello.urls'))
]