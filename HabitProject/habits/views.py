from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse,HttpRequest
from .models import Habit
# Create your views here.

def list_habit_items(request):
    context = {'habit_list':Habit.objects.all()}
    return render(request,'habits/habit_list.html',context)

def insert_habit_item(request:HttpRequest):
    habit=Habit(IndHabit =request.POST['habit'])
    habit.save()
    return redirect('/habits/list/')

def delete_habit_item(request,habit_id):
    habit_to_delete = Habit.objects.get(id=habit_id)
    habit_to_delete.delete()
    return redirect('/habits/list/')
    
def increment_habit_value(request,habit_id):
    habit_to_increment = Habit.objects.get(id=habit_id)
    habit_to_increment.IndValue += 1
    habit_to_increment.save()
    return redirect('/habits/list/')

def decrement_habit_value(request,habit_id):
    habit_to_decrement = Habit.objects.get(id=habit_id)
    habit_to_decrement.IndValue -= 1
    habit_to_decrement.save()
    return redirect('/habits/list/')
