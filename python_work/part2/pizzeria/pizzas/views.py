from django.shortcuts import render

from .models import Pizza


def index(request):
    """The home page for Pizzas."""
    return render(request, 'pizzas/index.html')


def pizzas(request):
    """Page that displays all pizzas."""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)
