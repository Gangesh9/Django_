from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='Contact us'),
    path('calculator/',views.calculator),
    path('odd_even/',views.even_odd),
    # path('serach/', views.contact,name='search')
]
