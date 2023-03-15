from django.shortcuts import render


def show_order(request):
    context = {}
    return render(request, 'order.html', context=context)
