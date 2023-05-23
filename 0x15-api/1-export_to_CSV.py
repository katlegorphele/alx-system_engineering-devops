#!/usr/bin/python3

'''
Export data in the CSV format.
'''

import sys
import requests

if __name__ == '__main__':
    emp_id = sys.argv[1]
    api_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
    response = requests.get(api_url)
    emp_username = response.json().get('username')

    todo_URL = f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos'
    response = requests.get(todo_URL)
    todo_list = response.json()

    with open(f'{emp_id}.csv', 'w') as f:
        for todo in todo_list:
            f.write('"{}","{}","{}","{}"\n'.format(
                emp_id,
                emp_username,
                todo.get('completed'),
                todo.get('title')
                ))
