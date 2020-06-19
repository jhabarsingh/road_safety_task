# Road_safety_task

## How To setUp on Linux

* Clone The Repo
* change directory to root folder
* install all the dependencies

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start the LocalHost server
* python manage.py runserver
* Install Postman
* make get Request to localhost:8000

## Check Api Using Postman
* [Install Postman](https://www.postman.com/downloads/)
* Create new workspace
* Select Get Api
* Paste localhost:8000/ping/ in input section
* Insert Query Params With keys as given below
>  * url 
>  * date_time
* Add Value of the above Query Params
* click on the send button

## Post Man
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


## Working
* A GET request (no parameters needed) is sent on the URL  specified (second parameter), when the current Date-Time matches the one specified in the Date-Time parameter (first parameter). The GETrequest on the URL parameter will only return a status code, and no response body. ( This Part is Handeled by celery and code is in the Views.py and Tasks.py file)

* Along with the API endpoints specified in each of the sets, a separate ping endpoint must be created, to know that the server is alive. Whenever a GET request is sent to the '/ping' endpoint, the server must return a JSON "{ "status":"OK"}".
( This Part code is in the Views.py file)
