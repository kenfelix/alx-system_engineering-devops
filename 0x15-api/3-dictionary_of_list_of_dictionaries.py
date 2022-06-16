#!/usr/bin/python3
"""
Get information about all user TODO progress.
Export data in the JSON format.
"""
import json
import requests

if __name__ == '__main__':

    base = 'https://jsonplaceholder.typicode.com/'
    user_url = base + 'users'
    users = requests.get(user_url).json()
    todo_url = base + 'todos'

    file = 'todo_all_employees.json'
    # For every user pick their todos
    # Conver list of todos to json
    with open(file, 'w') as f:
        json.dump({user.get('id'): [{
            'task': item.get('title'),
            'completed': item.get('completed'),
            'username': user.get('username')
            } for item in requests.get(todo_url,
                                       params={"userId": user.get('id')}
                                       ).json()] for user in users}, f)
