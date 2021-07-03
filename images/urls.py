from django.conf.urls import url
from . import views

# setting the url patterns

urlpatterns =[
    url('^$', views.welcome, name='welcome'),
]