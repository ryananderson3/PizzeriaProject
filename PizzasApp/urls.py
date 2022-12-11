from django.urls import path

from . import views

app_name = 'PizzasApp'

urlpatterns = [
    path('',views.index,name='index'),
    path('menu',views.menu,name='menu'),
    path('pizzas/<int:pizza_id>/',views.pizza,name='pizza'),
    path('new_comment/<int:pizza_id>/',views.new_comment,name='new_comment'),
]