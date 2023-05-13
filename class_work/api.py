import requests

response = requests.get(f'https://jsonplaceholder.typicode.com/posts/')
posts = response.json()
print(posts)

for key in posts:
  print(key, + ', ' + value)
