from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.user_list),
    path('login/', views.login_view, name='login'),
    path('delete-all-users/', views.delete_all_users, name='delete_all_users'),
    path('register/', views.create_multiple_dummy_users, name='create_multiple_dummy_users'),
]