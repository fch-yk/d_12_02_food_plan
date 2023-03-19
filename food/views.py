from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.utils.timezone import localdate, localtime
from django.views import View

from food.models import Dish, DishCategory, Meal, Sale, Subscription


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
    if not request.user.is_authenticated:
        return redirect('users:login')

    subscriptions = Subscription.objects.all().order_by('duration')
    sum = subscriptions[0].price if subscriptions.exists() else 0

    context = {
        'dish_categories': DishCategory.objects.all(),
        'subscriptions': subscriptions,
        'meals': Meal.objects.all(),
        'sum': sum,
    }

    return render(request, 'food/order.html', context=context)


def post_order(request):
    allergies_ids = [
        str(dish_category.id) for dish_category in DishCategory.objects.all()
        if request.POST.get(f"allergy_{dish_category.id}")
    ]

    meals_ids = [
        str(meal.id) for meal in Meal.objects.all()
        if request.POST.get(f'meal_{meal.id}')
    ]

    subscription_id = int(request.POST.get("term").split(';')[0])
    sum = Subscription.objects.get(id=subscription_id).price

    context = {
        'allergies': ','.join(allergies_ids),
        'meals': ','.join(meals_ids),
        'subscription': subscription_id,
        'sum': sum,
        'persons_number': request.POST.get('persons_number'),
    }
    return render(request, 'food/payment.html', context=context)


def pay(request):
    user = get_user_model().objects.get(id=request.user.id)

    allergies = request.POST.get('allergies')
    if allergies:
        allergies_ids = [int(id) for id in allergies.split(',')]
        user.allergy_to.set(
            DishCategory.objects.filter(id__in=allergies_ids)
        )
    else:
        user.allergy_to.clear()

    meals = request.POST.get('meals')
    if meals:
        meals_ids = [int(id) for id in meals.split(',')]
        user.meals.set(
            Meal.objects.filter(id__in=meals_ids)
        )
    else:
        user.meals.clear()

    subscription = Subscription.objects.get(
        id=int(request.POST.get('subscription'))
    )
    user.subscription = subscription
    user.persons_number = int(request.POST.get('persons_number'))
    user.subscription_start_at = localdate()
    user.save(
        update_fields=[
            'subscription',
            'persons_number',
            'subscription_start_at'
        ]
    )

    Sale.objects.create(
        sum=subscription.price,
        payed_at=localtime(),
        user=user,
    )

    context = {}
    return render(request, 'food/payment_success.html', context=context)


def show_sales_report(request):
    return redirect('users:login')
