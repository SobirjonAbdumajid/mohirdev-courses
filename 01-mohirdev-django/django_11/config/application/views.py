from django.shortcuts import render
from .models import Customer

# Create your views here.

def customer_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        address = request.POST.get('address')
        customer = Customer(name=name, surname=surname, age=age, address=address)
        customer.save()
    return render(request, 'customer_add.html')

def customer_list(request):
    context = {
        'customers': Customer.objects.all()
    }
    return render(request, 'customer_list.html', context)

def customer_update(request):
    if request.method == 'POST':
        customer_id = request.POST.get('id')
        customer = Customer.objects.get(id=customer_id)
        customer.name = request.POST('name')
        customer.surname = request.POST('surname')
        customer.age = request.POST('age')
        customer.address = request.POST('address')
        customer.save()
    return render(request, 'customer_page.html')

def customer_delete(request):
    if request.method == 'POST':
        customer_id = request.POST['id']
        customer = Customer.objects.get(id=customer_id)
        print(customer)
        customer.delete()
    return render(request, 'customer_delete.html')
def customer_page(request):
    return render(request,'customer_page.html')