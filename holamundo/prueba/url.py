from django.urls import path
from .views import *

urlpatterns = [
    path('contact/' , ContactView.createUser),
    path('turistic/', ContactView.getTuristic),
    

]