from django.contrib import admin
from django.urls import path
from foodz import views

urlpatterns = [
    path('',views.home,name='home'),
    path('review',views.review,name='review'),
    path('save',views.save,name='save'),
    path('br',views.br,name='br'),
    path('roti',views.roti,name='roti'),
    path('puri',views.puri,name='puri'),
    path('ice',views.ice,name='ice'),
    path('pav',views.pav,name='pav'),
]
