from django.shortcuts import render
from django.http import JsonResponse
from users_api_service.serve_users import UserServer
import json
import sqlite3
import os

# Create your views here.

RESPONSE_DATA_FILE = os.getcwd() + '/api_response/RESPONSE_JSON/api_responses.json'

with open(RESPONSE_DATA_FILE) as R:
    RESPONSE_DATA = json.load(R)

class UsersViews:

    def __init__(self):
        pass

    def default_api_response(self, request, *args, **kwargs):
        """ api endpoint response """
        return JsonResponse(RESPONSE_DATA['api_endpoint'], json_dumps_params = {'indent' : 4}, safe=False)


    def api_user_data(self, request, userid=None):
        user_details = UserServer().get_user_data(userid)
        
        response_data = {
        'status' : 'Success',
        'id' : f'{userid}',
        'User Details': user_details,
        }
        return JsonResponse(response_data, json_dumps_params = {'indent' : 4}, safe=False)

    def api_users(self,request):        
        user_details = UserServer().get_users()
    
        response_data = {
        'status' : 'Success',
        'Users': user_details,
        'Info': 'Some operations are expensive for server to calculate, fetch individual user to get detailed info.',
        }
        return JsonResponse(response_data, json_dumps_params = {'indent' : 4}, safe=False)




# ---------------------------------------------------------------------------------------------

def error404(request,exception):
    response_data = {
    'status' : 'Failed!',
    'Info': '404 Not Found',
    }
    return JsonResponse(response_data, json_dumps_params = {'indent' : 4}, safe=False)

def error500(request):
    response_data = {
    'status' : 'Failed!',
    'Info': '500 internal server error',
    }
    return JsonResponse(response_data, json_dumps_params = {'indent' : 4}, safe=False)


