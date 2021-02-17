# example from - https://www.w3schools.com/python/ref_requests_post.asp

import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data = myobj)

print(x.text)

print(x)