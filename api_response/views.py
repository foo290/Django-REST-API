from django.shortcuts import render
from django.http import JsonResponse
import json
import sqlite3

# Create your views here.
database_file = r'C:\Users\ns290\PycharmProjects\main_site\old versions\test_project\projectsite/studentdatabase_file.db'

RESPONSE_DATA_FILE = r'C:\Users\ns290\PycharmProjects\main_site\old versions\test_project\projectsite\api_response\RESPONSE_JSON/api_responses.json'
with open(RESPONSE_DATA_FILE) as R:
    RESPONSE_DATA = json.load(R)

def test_api(request, *args, **kwargs):
    
    # print(request.META)
    
    response_data = {
        'data' : f'{kwargs}',
    }

    return JsonResponse(response_data, json_dumps_params = {'indent' : 4}, safe=False)



# =================================================================================================
dummy = range(1000)
# =================================================================================================
# =================================================================================================

def get_users():
    try:
        connection = sqlite3.connect(database_file)
        cur = connection.cursor()
        raw = cur.execute(f'select name from students limit 5')
        data = raw.fetchall()
        data_list = [name[0] for name in data]
        data_list.append('more...')
        
        return data_list
    except Exception as error:
        return 'data not found'



def get_user_data(userid):

    """
    This function runs two query in sqlite database for getting the columns names and user details.
    It is for sqlite3 only.
    """

    try:
        connection = sqlite3.connect(database_file)
        cur = connection.cursor()
        cols = cur.execute("PRAGMA table_info(students)")
        col_fetch = cols.fetchall() 
        col_list = [col[1] for col in col_fetch]

        raw = cur.execute(f'select * from students where roll_no="{userid}" ')
        data = raw.fetchall()[0]
        structured_data = {col:detail for col,detail in zip(col_list,data)}

        return structured_data
    except Exception as error:
        return 'data not found'

# print(type(get_user('AC1031700')))

def default_api_response(request, *args, **kwargs):
    
    """ This gives the default response to api """
    api_path_end = str(request.path).split('/')[-2]

    print(api_path_end)

    if api_path_end == 'users':
        return JsonResponse(RESPONSE_DATA['user_api_endpoint'], json_dumps_params = {'indent' : 4}, safe=False)

    return JsonResponse(RESPONSE_DATA['api_endpoint'], json_dumps_params = {'indent' : 4}, safe=False)


def api_user_data(request, userid=None):

    user_details = get_user_data(userid)
    
    response_data = {
    'status' : 'Success',
    'id' : f'{userid}',
    'User Details': user_details,
    }

    return JsonResponse(response_data, json_dumps_params = {'indent' : 4}, safe=False)


def api_users(request):
    
    user_details = get_users()
    
    response_data = {
    'status' : 'Success',
    'Users': user_details,
    'Info': 'Some operations are expensive for server to calculate, fetch individual user to get detailed info.',
    }

    return JsonResponse(response_data, json_dumps_params = {'indent' : 4}, safe=False)


def error404(request,exception):
    response_data = {
    'status' : 'Failed!',
    'Info': '404 Not Found',
    }
    return JsonResponse(response_data, json_dumps_params = {'indent' : 4}, safe=False)


