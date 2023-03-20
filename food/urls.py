from django.urls import path

from .views import DishDetailView, Index, UserRecieptsView, dislike, like, post_order, show_order, pay,\
    show_sales_report

app_name = 'food'

urlpatterns = [
    path('', Index.as_view(), name='main'),
    path('dishes/', UserRecieptsView.as_view(), name='dishes_list'),
    path('dish/<int:pk>/', DishDetailView.as_view(), name='dish_detail'),
    path('order/', show_order, name='show_order'),
    path('order/postorder', post_order, name='post_order'),
    path('order/pay', pay, name='pay'),
    path('like/<int:pk>/', like, name='like'),
    path('dislike/<int:pk>/', dislike, name='dislike'),
    path('saleseport/', show_sales_report, name='show_sales_report'),

]
