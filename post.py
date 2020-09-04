import requests

post_data = {'name': 'Gladys'}
response = requests.post('http://127.0.0.1:8000/webhook/reverse-api-request/callback-point/github/', data=post_data)
