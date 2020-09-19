from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .user_server_api import GetUser
from . import api_app_settings
from .api_response_server import ResponseServer
from .json_responses import ApiDefaultResponses

# ---------------------------------------------------------------------------------------


@csrf_protect
def user_api_endpoint(request):
    response_data = ApiDefaultResponses.USER_API_ENDPOINT

    return JsonResponse(response_data, json_dumps_params={'indent': 4}, safe=False)


@csrf_protect
def default_api_response(request, *args, **kwargs):
    """ api endpoint response """

    response_data = ApiDefaultResponses.API_ENDPOINT

    if api_app_settings.DEBUG:
        response_data = ApiDefaultResponses.API_ENDPOINT_DEBUG

    return JsonResponse(response_data, json_dumps_params={'indent': 4}, safe=False)


def check_id_type(userid):
    try:
        int(userid)
        return 1
    except:
        return 0


@csrf_protect
def api_user_data(request, userid=None):
    if request.method == 'GET':
        if userid:
            if check_id_type(userid):
                user_details = GetUser().get_user(userid, keytype='id')
            else:
                user_details = GetUser().get_user(userid)
            if user_details:
                response_data = {
                    'status': 200,
                    'id': f'{userid}',
                    'details': user_details
                }
            else:
                response_data = {
                    'status': 404,
                    'id': f'{userid}',
                    "Message": "User with this identifier does not exist."
                }
            return JsonResponse(response_data, json_dumps_params={'indent': 4}, safe=False)
    else:
        pass


# ---------------------------------------------------------------------------------------------

def respond_to_call(request, **kwargs):
    params = kwargs
    app_label = params.pop('app_name')
    model_name = params.pop('model_name')

    data = ResponseServer().get_response(app_label, model_name, params)
    if data:
        response_data = {
            'status': 200,
            'info': data
        }
    else:
        response_data = {
            'status': 404,
            'info': 'Data not found for specified credentials.'
        }
    return JsonResponse(response_data, json_dumps_params={'indent': 4}, safe=False)


def error404(request, exception):
    response_data = ApiDefaultResponses.ERROR_404
    return JsonResponse(response_data, json_dumps_params={'indent': 4}, safe=False)


def error500(request, exception):
    response_data = ApiDefaultResponses.ERROR_500
    return JsonResponse(response_data, json_dumps_params={'indent': 4}, safe=False)
