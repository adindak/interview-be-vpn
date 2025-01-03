from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.payment_list),
    path('login/', views.login_view, name='login'),
    path('register/', views.create_multiple_dummy_payments, name='create_multiple_dummy_payments'),
]