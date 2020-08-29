# Django-REST-api
Underdevelopment
user api endpoint

### User data
Command

```
curl http://127.0.0.1:8000/api/domain/users/
```

Output

```
$ curl http://127.0.0.1:8000/api/domain/users/
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   267  100   267    0     0  16687      0 --:--:-- --:--:-- --:--:-- 16687{
    "status": "Success",
    "Users": [
        "Ritik",
        "Ankita",
        "Ankit",
        "Ankit",
        "Sagar",
        "more..."
    ],
    "Info": "Some operations are expensive for server to calculate, fetch individual user to get detailed info."
}
```

Command : fetch individual student by roll no.

```
curl http://127.0.0.1:8000/api/domain/users/AC10317009
```

```
$ curl http://127.0.0.1:8000/api/domain/users/AC10317009/
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   842  100   842    0     0   274k      0 --:--:-- --:--:-- --:--:--  274k{
    "status": "Success",
    "id": "AC10317009",
    "User Details": {
        "name": "Sarthak",
        "surname": "Gupta",
        "roll_no": "AC10317009",
        "course": "B.Tech",
        "branch": "CSE",
        "year": "1st year",
        "semester": "1st semester",
        "father_name": "Sanjay",
        "mothername": "Gupta",
        "father_phone": 910074****,
        "dob": "1999-03-02",
        "phone_no": 9271283411,
        "email": "sarthak****@gmail.com",
        "country": "India",
        "city": "Rohtak",
        "pin_code": ****,
        "adhaar": 89648430****,
        "dateofreg": "2017-04-04",
        "session": "2017-2021",
        "gender": "Male",
        "fee": 65000,
        "transport": "Yes",
        "address": "houseno.-50 block D pocket18 sector20\n",
        "docs": "['No Documents']"
    }
}
```

The data shown above is dummy and not specific to someone.

Command : Invalid command

```
curl http://127.0.0.1:8000/api/domain/blah.../
```

```
$ curl http://127.0.0.1:8000/api/domain/user/
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    56  100    56    0     0  28000      0 --:--:-- --:--:-- --:--:-- 56000{
    "status": "Failed!",
    "Info": "404 Not Found"
}
```

Underdevelopment!
