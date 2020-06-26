from django.shortcuts import render

from .models import Pizza, Toppings


def index(request):
    """The home page for Pizzas."""
    return render(request, 'pizzas/index.html')


def pizzas(request):
    """Page that displays all pizzas."""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)


def pizza(request, pizza_id):
    """Page that displays the toppings for a pizza."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.toppings_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings, }
    return render(request, 'pizzas/pizza.html', context)
