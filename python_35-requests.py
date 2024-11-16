# !pip install requests

import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

print(f"Response Status Code: {response.status_code}")
print(f"Response Content: {response.json()}")


url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post(url, json=data)

print(f"Response Status Code: {response.status_code}")
print(f"Response Content: {response.json()}")


url = "https://jsonplaceholder.typicode.com/posts"
params = {
    "userId": 1
}

response = requests.get(url, params=params)

print(f"Response Status Code: {response.status_code}")
print(f"Response Content: {response.json()}")


url = "https://httpbin.org/post"
form_data = {
    "name": "Someone",
    "age": 100
}

response = requests.post(url, data=form_data)

print(f"Response Status Code: {response.status_code}")
print(f"Response Content: {response.json()}")


url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:
    print(f"Success! Response Status Code: {response.status_code}")
    print(f"Response Content: {response.json()}")
else:
    print(f"Error! Response Status Code: {response.status_code}")


url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")


url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url, timeout=5)
    print(f"Response Status Code: {response.status_code}")
except requests.exceptions.Timeout:
    print("Request timed out")


url = "https://httpbin.org/post"
file = {'file': open('Files/read_example.txt', 'rb')}

response = requests.post(url, files=file)

print(f"Response Status Code: {response.status_code}")
print(f"Response Content: {response.json()}")


url = "https://httpbin.org/cookies"
response = requests.get(url, cookies={'name': 'Someone'})

print(f"Response Status Code: {response.status_code}")
print(f"Response Content: {response.json()}")