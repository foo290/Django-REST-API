# Default responses shown at api endpoints

class ApiDefaultResponses:
    USER_API_ENDPOINT = {
        'Welcome': 'This is user api endpoint. Here are somethings you can try...',
        'routes': [
            '/users/id/',
            '/users/username/'
        ],
    }

    API_ENDPOINT = {
        "WELCOME": "This is the api endpoint.",
        "suggested": "Start making request on API_URLS that you've specified",
    }

    API_ENDPOINT_DEBUG = {
        "WELCOME": "This is the api endpoint.",
        "suggested": "Start making request on API_URLS that you've specified. Here are somethings that you can try...",
        "Custom URL": 'You can define your custom url patterns for api in settings.py. '
                      'For more, read the instructions below...',
        "Link": '',
        "Debug info": 'YOU ARE GETTING THIS INSTRUCTED RESPONSE BECAUSE DEBUG IS SET True IN YOUR PROJECT.'
    }

    APP_ENDPOINT = {
        'info': [
            'Some operations may be expensive for server to compute. Request individual to get full details.',
        ]
    }

    APP_ENDPOINT_DEBUG = {
        'info': [
            'Some operations may be expensive for server to compute. Request individual to get full details.',
            'Only 10 of total results are displayed for this kind of request to pevent server overloading.',
            'This number can be increased or set to show all results by default by setting a variable in settins.py.',
            "Set a variable ENDPOINT_RESPONSE_LENGTH = define no. of results OR 'all' for display full results.",
            '-------------------------------------------------------------------------------------------',
            'YOU ARE GETTING THIS INSTRUCTED RESPONSE BECAUSE DEBUG IS SET True IN YOUR PROJECT.'
        ]
    }

    ERROR_404 = {
        'status': 404,
        'info': 'Specified url does not exist.'
    }

    ERROR_500 = {
        'status': 500,
        'info': 'Internal server error.'
    }
