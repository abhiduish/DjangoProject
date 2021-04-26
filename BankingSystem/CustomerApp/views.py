from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from CustomerApp.models import Customer
def index(request):
    content = "<h1>hello world this is Customer App</h1><br><br>"
    content = content+"<a href='all_customer/'>All Customer</a><br><br>"
    content = content+"<a href='add_customer/'>Add Customer</a><br><br>"
    return HttpResponse(content)

def all_customer(request):
    latest_customer_list = Customer.objects.all()

    context = {
       'latest_customer_list':latest_customer_list 
    }
    return render(request,'CustomerApp/customerlist.html',context)

def detail(request,customer_id):
    customer = get_object_or_404(Customer,pk=customer_id)
    context = {'customer':customer}
    return render(request,'CustomerApp/customerdetails.html',context)

def addcustomer(request):
    return render(request,'CustomerApp/addcustomer.html')

def deletecustomer(request,customer_id):
    customer = get_object_or_404(Customer,pk=customer_id)
    message = ""
    try:
        customer.delete()
        message = "Customer Record Deleted Successfully"
    except:
        message = "Customer Record Not Deleted. Please try again"
    return HttpResponse(message)

from django.utils import timezone

def add(request):
    name = request.POST['name']
    account_no = request.POST['account_no']
    gender = request.POST['gender']
    balance = request.POST['balance']
    address = request.POST['address']

    customer = Customer(name=name,account_no=account_no,gender=gender,balance=balance,address=address,pub_date=timezone.now())

    message = ""
    try:
        customer.save()
        message="Customer Register Successfully!!!"
    except:
        message="Customer Record not save,please try again"

    context = {'message':message}
    return render(request,'CustomerApp/addcustomer.html',context)

    #django rest framework

from django.shortcuts import render 
from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from .serializers import CustomerSerializer
@csrf_exempt
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors,status=400)
    

@csrf_exempt 
def customer_detail(request, pk):

    try:        
        customer = Customer.objects.get(pk=pk)

    except Customer.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)       
        return JsonResponse(serializer.data)
 
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(customer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        customer.delete()      
        return HttpResponse(status=204)