#!/usr/bin/python3

'''
Extending Task 0 functionality
'''

import json
import requests
from sys import argv

if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(api_url)
    users = response.json()

    emp_dict = {}
    for user in users:
        emp_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
        url = url + '/todos/'
        response = requests.get(url)
        
        todos = response.json()
        emp_dict[emp_id] = []
        for todo in todos:
            task_dict = {}
            task_dict['username'] = username
            task_dict['task'] = todo.get('title')
            task_dict['completed'] = todo.get('completed')
            emp_dict[emp_id].append(task_dict)

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(emp_dict, json_file)
