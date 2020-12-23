from django.urls import path

from . import views

urlpatterns =[
    path('',views.pictures,name='pictures'),
    path('location/<location>',views.location,name='location'),
    path('search/',views.search_results,name='search_results')
]