from django.shortcuts import render
# from django.http import HttpResponse
from first_app.models import Data
# Create your views here.

def tester(request):
    list_data=Data.objects.order_by('first_name')
    dict={'data':list_data}
    # return HttpResponse("<em>Hello</em>")
    return render(request,'first_app/index.html',context=dict)