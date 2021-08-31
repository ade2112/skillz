import requests

r = requests.get('https://api.github.com/user', auth=('solomonmarvel97', '12345'))
print(r.status_code)
print(r.headers['content-type'])
# print(r.json())