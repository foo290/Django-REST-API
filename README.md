# Django-REST-api

Django-REST-API is an app which lets you make get request for getting user information specified by userid or username.

### Installation
clone the repo and run the following command where "dist" dir is:
```
python -m pip install dist/Django-REST-0.1.tar.gz
```


Quick start
-----------

1. Add "api_response" to your INSTALLED_APPS setting like this::

```
INSTALLED_APPS = [
    ...
    api_response,
]
```

2. Include the polls URLconf in your project urls.py like this:

```
import api_response
path('api.yourDomain/', include('api_response.urls')),
```
 
YOU CAN CHANGE THE URL PATTERN HERE ACCORDING TO YOUR PREFERANCE
BUT DON'T FORGET TO ADD "/users" WHILE MAKING API REQUESTS AT THE END.
FOR EX:
```
http://127.0.0.1:8000/YOUR_PATTERN/users/ "id OR username"
```

3. Start the development server and visit ```http://127.0.0.1:8000/api.yourDomain/```

5. To request user info visit:

```
http://127.0.0.1:8000/api.yourDomain/users/id/
    OR
http://127.0.0.1:8000/api.yourDomain/users/username_here/
```
#### You can request userinfo either by username or id.

6. If you have a user profile app which extends django default user configurations, then to merge profile add following to your settings.py::

```
INCLUDE_PROFILE = True
PROFILE_MODEL = your_profile_model here // can be found at your profile.models
```

you can set profile model class like:
```
just specify the name of class which has one-to-one relation with user like:

INCLUDE_PROFILE = True
PROFILE_MODEL = 'profile'
```

## Output

#### Without profile model
```
$ curl http://127.0.0.1:8000/api.domain/users/1/
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   319  100   319    0     0  53166      0 --:--:-- --:--:-- --:--:-- 53166{
    "status": "Success",
    "id": "1",
    "details": {
        "id": 1,
        "last_login": "2020-09-13T07:56:22.792Z",
        "username": "ns290",
        "first_name": "",
        "last_name": "",
        "email": "ns@gmail.com",
        "is_active": true,
        "date_joined": "2020-09-13T05:57:07Z"
    }
}
```

### After adding profile model to settings.py like: 
```
INCLUDE_PROFILE = True
PROFILE_MODEL = 'profile'
```

```
$ curl http://127.0.0.1:8000/api.domain/users/1/
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   554  100   554    0     0  61555      0 --:--:-- --:--:-- --:--:-- 61555{
    "status": "Success",
    "id": "1",
    "details": {
        "id": 1,
        "last_login": "2020-09-13T07:56:22.792Z",
        "username": "ns290",
        "first_name": "",
        "last_name": "",
        "email": "ns@gmail.com",
        "is_active": true,
        "date_joined": "2020-09-13T05:57:07Z",
        "img": "/Media/default_pfp.jpg",
        "bio": null,
        "city": null,
        "country": null,
        "company": null,
        "github": null,
        "twitter": null,
        "instagram": null,
        "website": null
    }
}
```
#### For uninstall, run the following command:
```
python -m pip uninstall Django-REST
```






