from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from users_api_service.serve_users import UserServer
import json
import sqlite3
import os
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect



# Create your views here.

RESPONSE_DATA_FILE = os.getcwd() + '/api_response/RESPONSE_JSON/api_responses.json'

with open(RESPONSE_DATA_FILE) as R:
    RESPONSE_DATA = json.load(R)



# ---------------------------------------------------------------------------------------

class GetUser:
    def __init__(self):
        pass
    
    def get_user(self, p_key, keytype = 'username'):
        
        if p_key:
            if keytype == 'username':
                user = User.objects.filter(username = p_key)
            elif keytype == 'id':
                user = User.objects.filter(id = p_key)
            else:
                return 'Not a vaid keytype'

            if user:
                user = user[0]
                vals = [
                    user.username,
                    user.first_name,
                    user.last_name,
                    user.profile.img.url,
                    user.email,
                    user.profile.twitter,
                    user.profile.github
                ]
                
                keys = 'username-first name-last name-image-email-twitter-github'.split('-')

                data = {k:v for k,v in zip(keys, vals)}

                
                return data

            else:
                return False
        else:
                return False
            

        



















@csrf_protect
def default_api_response(request, *args, **kwargs):
    """ api endpoint response """
    return JsonResponse(RESPONSE_DATA['api_endpoint'], json_dumps_params = {'indent' : 4}, safe=False)

@csrf_protect
def api_user_data(request, userid=None):
    # user_details = UserServer().get_user_data(userid)
    if request.method == 'GET':
        if userid:
            try:
                userid = int(userid)
                user_details = GetUser().get_user(userid, keytype='id')
            except:
                user_details = GetUser().get_user(userid)
            

            if user_details:
                response_data = {
                'status' : 'Success',
                'id' : f'{userid}',
                }
                response_data.update(user_details)
            else:
                response_data = {
                    
                    'id' : f'{userid}',
                }
                response_data.update(RESPONSE_DATA['user_id_not_found'])
            return JsonResponse(response_data, json_dumps_params = {'indent' : 4}, safe=False)
    else:
        pass

@csrf_protect
def api_users(request):
    if request.method == 'GET':    
        user_details = UserServer().get_users()

        response_data = {
        'status' : 'Success',
        'Users': user_details,
        'Info': 'Some operations are expensive for server to calculate, fetch individual user to get detailed info.',
        }
        return JsonResponse(response_data, json_dumps_params = {'indent' : 4}, safe=False)
    else:
        pass



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


def test(request):
    print(request.headers)
    return HttpResponse('')