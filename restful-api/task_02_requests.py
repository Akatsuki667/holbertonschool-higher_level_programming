#!/usr/bin/python3
import requests


def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = posts = response.json()

    for post in posts:
        print(post['title'])


def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = posts = response.json()

        filtered_posts = []

        for post in posts:
            filtered_post = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            filtered_posts.append(filtered_post)

        for post in filtered_posts[:5]:  # Afficher les 5 premiers posts
            print(post)

    else:
        print("Échec de la requête, code:", response.status_code)
