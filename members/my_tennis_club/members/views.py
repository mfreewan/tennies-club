from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
#members function to return a Httpresponse 
def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render({}, request))