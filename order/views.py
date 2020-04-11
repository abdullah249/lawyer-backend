from django.shortcuts import render 
from .models import Orders
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.decorators import api_view
  
@api_view(['GET', 'POST'])
def read_orders(request):
    data = Orders.objects.all()
    data = list(data.values())
    return JsonResponse(data,safe=False)

@api_view(['GET', 'POST'])    
def add_orders(request):
	try:
		username = request.data.get('username',None)
	except MultiValueDictKeyError:
		return JsonResponse({"Error":"username is required"},status=500)	
	user = User.objects.get(username=username)
	obj  = Orders(title=title,description=description,price=price,user=user)
	return JsonResponse(list(obj),safe=False,status=200)	




@api_view(['POST'])
def getOrderofUser(request):
	username = request.data.get('username',None) 
	if username is None:
		return HttpResponse("Username is required")
	user = User.objects.get(username=username)
	Orders = Orders.objects.filter(lawyerid = lawyer).values()
	return JsonResponse(list(Orders),safe=False)

    