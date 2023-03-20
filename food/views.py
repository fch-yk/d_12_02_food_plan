from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.timezone import localdate, localtime
from django.views import View
from django.views.generic import ListView, DetailView

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


class UserRecieptsView(ListView):
    """Представление вывода списка рецептов для пользователя"""
    model = Dish
    paginate_by = 4

    def get_queryset(self):
        allergy_to = self.request.user.allergy_to.all().values_list('id', flat=True)
        disliked_dishes = self.request.user.disliked_dishes.all().values_list('id', flat=True)
        return super().get_queryset().exclude(categories__id__in=allergy_to).exclude(id__in=disliked_dishes)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Меню'
        return context


class DishDetailView(DetailView):
    """Представление просмотра рецепта"""
    model = Dish

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Просмотр рецепта'
        return context

@login_required(login_url='/users/login/')
def like(request, pk):
    dish = Dish.objects.get(pk=pk)
    is_like = False
    like_dishes = request.user.liked_dishes.all()
    if dish in like_dishes:
        is_like = False
        request.user.liked_dishes.remove(dish)
    else:
        is_like = True
        request.user.liked_dishes.add(dish)

    return JsonResponse({
        'is_like': is_like,
    })

@login_required(login_url='/users/login/')
def dislike(request, pk):
    dish = Dish.objects.get(pk=pk)
    is_dislike = False
    dislike_dishes = request.user.disliked_dishes.all()
    if dish in dislike_dishes:
        is_dislike = False
        request.user.disliked_dishes.remove(dish)
    else:
        is_dislike = True
        request.user.disliked_dishes.add(dish)

    return JsonResponse({
        'is_dislike': is_dislike,
    })


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
    if not request.user.is_authenticated:
        return redirect('users:login')

    sales = Sale.objects.annotate(
        month=TruncMonth('payed_at')).values('month').annotate(
            sum=Sum('sum')
    ).order_by('month')

    context = {
        'title': 'Продажи',
        'sales': sales,
        'total': Sale.objects.aggregate(Sum('sum'))['sum__sum'],
    }
    return render(request, 'food/sales.html', context=context)
