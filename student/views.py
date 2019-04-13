from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from center.models import *
from django.http import HttpResponse
from django.core.cache import cache

@csrf_exempt
def attendancefun(request):
		result=""
		Name=cache.get('my_key')
		rollno=Entity.objects.get(entityname=Name).rollno
		variable=attendance.objects.all()
		for val in variable:
			if(val.rollno==rollno):
				result= result+val.subject.subject+":"+str(val.attended)+","+str(val.totalclasses)
		print(result)
		return HttpResponse(result)
@csrf_exempt
def marks(request):
		result=""
		Name=cache.get('my_key')
		rollno=Entity.objects.get(entityname=Name).rollno
		variable=Marks.objects.all()
		for val in variable:
			if(val.rollno==rollno):
				result= result+val.subject.subject+":"+str(val.marks)
		print(result)
		return HttpResponse(result)

"""@csrf_exempt
def assingment(request):
		result=""
		Name=cache.get('my_key')
		course=Entity.objects.get(entityname=Name).course
		variable=exam.objects.all()
		for val in variable:
			if(val.rollno==rollno):
				result= result+val.subject.subject+":"+str(val.marks)
		print(result)
		return HttpResponse(result)
	"""

