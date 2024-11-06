from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CustomerSerializer
from app1.models import Customer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions

# Create your views here.
@api_view(['POST'])
def add_customer(request):
    new_customer = CustomerSerializer(data=request.data)
    if new_customer.is_valid():
        new_customer.save()
        return Response({'message': 'Added Successfully!'},status=200)
    return Response({'message': 'Something went wrong!'}, status=400)

@api_view(['GET'])
def list_customers(request):
    customers = Customer.objects.all()
    new_data_json = CustomerSerializer(customers, many=True)
    return Response(new_data_json.data)

@api_view(['DELETE'])
def customers_delete(request):
    customer = request.data
    customer_id = customer.get('id')
    xaridor = Customer.objects.get(id=customer_id)
    xaridor.delete()
    return Response({"message:": "Deleted successfully"}, status=200)

@api_view(['PUT'])
def customers_update(request):
    try:
        customer = request.data
        customer_id = customer.get('id')
        xaridor = Customer.objects.get(id=customer_id)
        xaridor.name = customer.get('name')
        xaridor.surname = customer.get('surname')
        xaridor.age = customer.get('age')
        xaridor.address = customer.get('address')
        xaridor.save()
        return Response({"message: ": "Updated successfully!"}, status=200)

    except Exception as e:
        return Response({"message: ": "Operations failed!"}, status=400)

# @api_view(['GET'])
# def customer_search(request):
#     try:
#         customer = request.data
#         customer_name = customer.get('name')
#         customer_surname = customer.get('surname')
#         # xaridor = Customer.objects.get(name=customer_name)
#         xaridor = Customer.objects.filter(name__icontains=customer_name) | Customer.objects.filter(name__icontains=customer_surname)
#         xaridor_json = CustomerSerializer(xaridor, many=True)
#         return Response(xaridor_json.data)
#     except Exception as e:
#         return Response({"message: ":"Operation Failed"}, status=400)

@api_view(["GET"])
def customer_search(request):
    try:
        customer = request.data
        customer_name = customer.get('name')
        # customer_surname = customer.get('surname')
        xaridor = Customer.objects.filter(name__icontains = customer_name)
        xaridor_json = CustomerSerializer(xaridor, many=True)
        return Response(xaridor_json.data)
    except:
        return Response({"message: ": "Operation Failed"}, status = 400)
