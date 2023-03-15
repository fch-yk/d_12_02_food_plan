from django.shortcuts import render


def view_index(request):
    return render(request, 'food/index.html')

def show_order(request):
    context = {}
    return render(request, 'order.html', context=context)

