from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View

from food.models import Dish, DishCategory


class Index(View):
    """Представление главной страницы"""
    template_name = 'food/index.html'

    def get(self, request, *args, **kwargs):
        dishes = Dish.objects.all()[:5]
        context = {
            'title': 'FoodPlan главная',
            'dishes': dishes
        }
        return render(request, self.template_name, context)


def show_order(request):
    dish_categories = DishCategory.objects.all()
    context = {
        'dish_categories': dish_categories
    }
    return render(request, 'food/order.html', context=context)


def post_order(request):

    allergies_ids = []
    dish_categories = DishCategory.objects.all()
    for dish_category in dish_categories:
        allergy_id = request.POST.get(f"allergy_{dish_category.id}")
        if allergy_id:
            allergies_ids.append(allergy_id)

    allergies = ','.join(allergies_ids)

    context = {'allergies': allergies}
    return render(request, 'food/payment.html', context=context)


def pay(request):
    user = get_user_model().objects.get(id=request.user.id)
    allergies = request.POST.get('allergies')

    if allergies:
        allergies_ids = [int(id) for id in allergies.split(',')]
        allergies = DishCategory.objects.filter(id__in=allergies_ids)
        user.allergy_to.set(allergies)

    context = {}
    return render(request, 'food/payment_success.html', context=context)
