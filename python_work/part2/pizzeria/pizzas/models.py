from django.db import models


class Pizza(models.Model):
    """A class for collecting different types of Pizza."""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Toppings(models.Model):
    """A class for the toppings for different pizzas."""
    pizza = models.ForeignKey(Pizza, on_delete=models.DO_NOTHING)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.name}, Pizza: {self.pizza}"
