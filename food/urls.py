from django.urls import path
from .views import view_index, show_order

app_name = 'food'

urlpatterns = [
    path('', view_index, name='index').
    path('order/', show_order, name='show_order'),
]
