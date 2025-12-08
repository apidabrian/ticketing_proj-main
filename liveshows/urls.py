from django.urls import path
from views import live_show_list    

urlpatterns = [
     path('', live_show_list, name='live_show_list'),       
    ]
