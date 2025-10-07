#!/usr/bin/python3
# import requests library
import requests
import csv


# Fetch posts from JSONPlaceholder
def fetch_and_print_posts():
    posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status code: {}".format(posts.status_code))
    if posts.status_code == requests.codes.ok:
        try:
            posts_json = posts.json()
            for post in posts_json:
                print(post["title"])
        except Exception as e:
            print(f"Exception occurred: {e}")
    else:
        posts.raise_for_status()


# Fetch and save posts to csv file
def fetch_and_save_posts():
    posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    if posts.status_code == requests.codes.ok:
        posts_json = posts.json()
        fields = posts_json[0].keys()

        with open("posts.csv", "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for post in posts_json:
                writer.writerow(post)
