# Road_safety_task

# How To setUp on Linux

* Clone The Repo
* change directory to root folder
* install all the dependencies

# Install Dependencies

```bash
pip install -r requirements.txt
```

# Start the LocalHost server
* python manage.py runserver
* Install Postman
* make get Request to localhost:8000
* params
>  * url 
>  * date_time

# Post Man
![Postman](https://raw.githubusercontent.com/jhabarsingh/road_safety_task/master/django_intern.png)

## Libraries Used
* Redis
* Celery( For asynchronous Task)


## View Code
```python
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
```

## Task Async
```python
from celery.decorators import task
from django.http import JsonResponse
import time
import datetime
@task(name="check")
def check(url, date_time):
	date_time = datetime.datetime(*date_time)
	time.sleep(date_time.timestamp()-datetime.datetime.now.timestamp()) #Wait For The Given Time And then executes the futher code	
	code = 404
	try:
		code = requests.get(url).status_code
	except Exception:
		pass
	return JsonResponse({'status':code})
```

