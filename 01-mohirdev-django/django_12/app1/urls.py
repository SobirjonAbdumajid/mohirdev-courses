from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add_customer),
    path('list/', list_customers),
    path('delete/', customers_delete),
    path('update/', customers_update),
    path('search/', customer_search),
]