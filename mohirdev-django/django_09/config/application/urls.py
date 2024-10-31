from django.urls import path, include
from .views import customer_page_function
urlpatterns = [
    path('customers/', customer_page_function)
]