from django.shortcuts import render
from django.http import HttpResponse


def view_index(request):
    return render(request, 'food/index.html')


def show_order(request):
    context = {}
    return render(request, 'order.html', context=context)


def post_order(request):
    # получаем из данных запроса POST отправленные через форму данные
    # name = request.POST.get("name", "Undefined")
    # age = request.POST.get("age", 1)
    # return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")
    return HttpResponse("Hello")
