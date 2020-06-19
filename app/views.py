from django.shortcuts import render
from django.http import JsonResponse
import requests
import datetime
from app import tasks 
# Create your views here.



def task(request, *args, **kwargs):
	if request.method == 'GET':
		url = request.GET['url']
		date_time = list(map(int, request.GET['date_time'][1:-1].split(',')))
		tasks.check.delay(url, date_time)
		return JsonResponse({'status': 200})
	return JsonResponse({'status':404})