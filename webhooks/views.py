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


# POST Request :
# $ curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/webhook/reverse-api-request/callback-point/github/
# data should be json
from allauth.app_settings import SOCIALACCOUNT_ENABLED

print(SOCIALACCOUNT_ENABLED)
