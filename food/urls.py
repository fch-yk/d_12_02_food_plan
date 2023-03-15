from django.urls import path
from .views import view_index

app_name = 'food'

urlpatterns = [
    path('', view_index, name='index')
]
