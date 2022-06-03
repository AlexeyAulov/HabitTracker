from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def list_habit_items(request):
    return HttpResponse('from list_habit_items')