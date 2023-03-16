from django.urls import path
from .views import Index, show_order

app_name = 'food'

urlpatterns = [
    path('', Index.as_view(), name='main'),
    path('order/', show_order, name='show_order'),
]
