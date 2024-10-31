from django.urls import path, include
from .views import customer_page

urlpatterns = [
    path('customers/', customer_page)
]