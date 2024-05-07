import requests

url = 'http://localhost:8000/add_user'
data = {"username": "Sasha", "user_info": "любит ебать"}

response = requests.post(url, data=data)
print(response.text)
