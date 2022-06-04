from django.urls import path
from . import views



urlpatterns=[
    path('list/',views.list_habit_items),
    path('insert_habit/',views.insert_habit_item,name='insert_habit_item'),
    path('delete_habit/<int:habit_id>',views.delete_habit_item,name='delete_habit_item'),
    path('increment_habit/<int:habit_id>',views.increment_habit_value,name='increment_habit_value'),
    path('decrement_habit/<int:habit_id>',views.decrement_habit_value,name='decrement_habit_value'),
    ]