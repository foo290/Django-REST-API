from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json

# Create your views here.

temp_data = []

def github_webhook_point(request):
    if request.method == 'POST':
        data_recived = request.body.decode('UTF-8')
        cleaned_data = json.loads(data_recived)
        temp_data.append(cleaned_data)



        return HttpResponse(b'200 : OK')
        pass