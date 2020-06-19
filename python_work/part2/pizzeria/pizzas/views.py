from django.shortcuts import render


def index(request):
    """The home page for Pizzas."""
    return render(request, 'pizzas/index.html')
