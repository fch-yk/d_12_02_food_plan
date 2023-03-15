from django.urls import path


from food import views


urlpatterns = [
    path('order/', views.show_order),
]
