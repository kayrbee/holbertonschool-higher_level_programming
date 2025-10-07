#!/usr/bin/python3
# import requests library
import requests


# Fetch posts from JSONPlaceholder
p = requests.get('https://jsonplaceholder.typicode.com/posts')
print("Status code: {}".format(p.status_code))
if p.status_code >= 200 and p.status_code < 300:
    print(p.json())
# Fetch and save posts to csv file