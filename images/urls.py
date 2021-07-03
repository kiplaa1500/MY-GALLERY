from django.conf.urls import url
from . import views

# setting the url patterns

urlpatterns =[
    url(r'^$', views.my_gallery, name = 'myGallery'),
    url(r'^search$', views.search_results, name='search_results'),
    url(r'^search/location$', views.search_location, name='search_location'),
]