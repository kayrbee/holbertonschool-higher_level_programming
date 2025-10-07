#!/usr/bin/python3
# import requests library
import requests


# Fetch posts from JSONPlaceholder
posts = requests.get('https://jsonplaceholder.typicode.com/posts')
print("Status code: {}".format(posts.status_code))
if posts.status_code >= 200 and posts.status_code < 300:
    posts_json = posts.json()
    for post in posts_json:
        print(post["title"])
# Fetch and save posts to csv file