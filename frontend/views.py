from django.shortcuts import render
from center.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.http import HttpResponse
# Create your views here.

@csrf_exempt
def index(request):
    	if(request.method=="GET"):
            return render(request,'frontend/index.html')
    	elif(request.method=="POST"):
            Name = request.POST.get('name')
            Password= request.POST.get('Password')
            if(Name != None and Password != None):
                namecheck=(Login.objects.get(username=Name))
                if(namecheck.password==Password):
                    cache.set('my_key',Name,30)
                    if(namecheck.entity=="Teacher"):
                        return render(request,'frontend/Teacher.html')
                    else:
                        return render(request,'frontend/Student.html')
                else:
                    return HttpResponse("Login Unsuccessful")
            else:
                return HttpResponse("Login Unsuccessful")
