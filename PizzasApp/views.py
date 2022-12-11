from django.shortcuts import render,redirect    #allows you to render a page and redirect a page
from .models import *
from .forms import *
from email.mime import image

# Create your views here.
def index(request):
    return render(request, 'PizzasApp/index.html')

def menu(request):
    pizzas = Pizza.objects.order_by('-pizza_name')  # pizza_name is a column in the Pizza class in models.py

    context = {'all_pizzas':pizzas}     # the key is the variable name you will use in your html file
                                        # the value is the variable name you are using in the view

    return render(request, 'PizzasApp/menu.html', context)

def pizza(request, pizza_id):           # loads each individual topic and its information
    p = Pizza.objects.get(id=pizza_id)
    t = Toppings.objects.filter(pizza=p)
    c = Comments.objects.filter(pizza=p)
    image = Pizza.image

    context = {'pizza':p, 'toppings':t, 'comments':c,'image':image}

    return render(request, 'PizzasApp/pizza.html', context)

def new_comment(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        print(request.POST)
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = p
            new_comment.save()

            return redirect('PizzasApp:pizza',pizza_id=pizza_id)
    
    context = {'form':form, 'pizza':p}
    return render(request, 'PizzasApp/new_comment.html', context)


