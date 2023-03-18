from django.shortcuts import render
from django.views import View

from food.models import Dish


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
    context = {}
    return render(request, 'food/order.html', context=context)


def post_order(request):
    # получаем из данных запроса POST отправленные через форму данные
    # name = request.POST.get("name", "Undefined")
    # age = request.POST.get("age", 1)
    # return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")
    context = {}
    return render(request, 'food/payment.html', context=context)


def pay(request):
    context = {}
    return render(request, 'food/payment_success.html', context=context)
