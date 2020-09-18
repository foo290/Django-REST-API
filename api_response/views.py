from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
import sqlite3
import os
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from .user_server_api import GetUser
from . import api_app_settings




# Create your views here.
api_base_dir = os.path.dirname(os.path.abspath(__file__))

RESPONSE_DATA_FILE = api_base_dir + '/RESPONSE_JSON/api_responses.json'

with open(RESPONSE_DATA_FILE) as R:
    RESPONSE_DATA = json.load(R)



# ---------------------------------------------------------------------------------------




@csrf_protect
def default_api_response(request, *args, **kwargs):
    """ api endpoint response """
    return JsonResponse(RESPONSE_DATA['api_endpoint'], json_dumps_params = {'indent' : 4}, safe=False)

def check_id_type(userid):
    try:
        userid = int(userid)
        return 1
    except:
        return 0

@csrf_protect
def api_user_data(request, userid=None):
    # user_details = UserServer().get_user_data(userid)
    if request.method == 'GET':
        if userid:

            test = GetUser()
            test.MERGE_PROFILE_INFO = api_app_settings.INCLUDE_PROFILE
            test.PROFILE_MODEL = api_app_settings.PROFILE_MODEL
            
            if check_id_type(userid):
                user_details = test.get_user(userid, keytype='id')
            else:
                user_details = test.get_user(userid)

            if user_details:
                response_data = {
                'status' : 'Success',
                'id' : f'{userid}',
                }
                response_data['details']=user_details

            else:
                response_data = {
                    
                    'id' : f'{userid}',
                }
                response_data.update(RESPONSE_DATA['user_id_not_found'])
            return JsonResponse(response_data, json_dumps_params = {'indent' : 4}, safe=True)
    else:
        pass

# ---------------------------------------------------------------------------------------------

# def error404(request,exception):
#     response_data = {
#     'status' : 'Failed!',
#     'Info': '404 Not Found',
#     }
#     return JsonResponse(response_data, json_dumps_params = {'indent' : 4}, safe=False)

# def error500(request):
#     response_data = {
#     'status' : 'Failed!',
#     'Info': '500 internal server error',
#     }
#     return JsonResponse(response_data, json_dumps_params = {'indent' : 4}, safe=False)


# def test(request):
#     print(request.headers)
#     return HttpResponse('')

