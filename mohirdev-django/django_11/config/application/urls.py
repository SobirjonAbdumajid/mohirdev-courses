from django.urls import path
from .views import *

urlpatterns = [
    path('customers/', customer_page),
    path('update/', customer_update),
    path('add/', customer_add),
    path('list/', customer_list),
    path('delete/', customer_delete),
]