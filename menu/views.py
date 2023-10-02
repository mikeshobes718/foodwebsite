from django.shortcuts import render
from .models import FoodItem
from menu import views

def index(request):
    # Fetch all FoodItem objects from the database
    featured_dishes = FoodItem.objects.all()

    # Pass the data to the template
    context = {
        'featured_dishes': featured_dishes
    }
    return render(request, 'menu/index.html', context)
