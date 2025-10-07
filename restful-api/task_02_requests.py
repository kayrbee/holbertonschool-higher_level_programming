#!/usr/bin/python3
# import requests library
import requests


# Fetch posts from JSONPlaceholder
p = requests.get('https://jsonplaceholder.typicode.com/posts')
print("Status code: {}".format(p.status_code))
# Fetch and save posts to csv file