from celery.decorators import task
from django.http import JsonResponse
import time
import datetime
@task(name="check")
def check(url, date_time):
	date_time = datetime.datetime(*date_time)
	time.sleep(date_time.timestamp()-datetime.datetime.now.timestamp())	
	code = 404
	try:
		code = requests.get(url).status_code
	except Exception:
		pass
	return JsonResponse({'status':code})