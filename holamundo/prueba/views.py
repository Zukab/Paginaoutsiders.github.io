from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response


def homePageView(request):
    return Response({'message': 'quintero es gay'})

def aboutPageView(request):
    return HttpResponse("about")