from django.shortcuts import render
from .models import *

# Create your views here.
def customer_page_function(request):
    context = {
        'customers': Customer.objects.all(),
    }
    return render(request, "customer_list.html", context)