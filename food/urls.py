from django.urls import path

from .views import Index, post_order, show_order, pay, show_sales_report

app_name = 'food'

urlpatterns = [
    path('', Index.as_view(), name='main'),
    path('order/', show_order, name='show_order'),
    path('order/postorder', post_order, name='post_order'),
    path('order/pay', pay, name='pay'),
    path('saleseport/', show_sales_report, name='show_sales_report'),

]
