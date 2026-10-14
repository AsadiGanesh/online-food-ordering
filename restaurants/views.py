from django.shortcuts import render, get_object_or_404

from .models import Restaurant, Category, Food


def restaurant_list(request):
    restaurants = Restaurant.objects.filter(is_active=True)

    return render(
        request,
        "restaurants/restaurant_list.html",
        {"restaurants": restaurants}
    )


def restaurant_menu(request, restaurant_id):
    restaurant = get_object_or_404(
        Restaurant,
        id=restaurant_id,
        is_active=True
    )

    categories = Category.objects.filter(
        restaurant=restaurant
    )

    foods = Food.objects.filter(
        restaurant=restaurant,
        is_available=True
    )

    return render(
        request,
        "restaurants/menu.html",
        {
            "restaurant": restaurant,
            "categories": categories,
            "foods": foods,
        }
    )