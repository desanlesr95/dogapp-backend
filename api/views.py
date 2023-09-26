from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def get(request):
    name = [{'name','Luis'}]
    return JsonResponse(name, safe=False)