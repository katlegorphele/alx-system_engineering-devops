#!/usr/bin/python3

'''
Export data in JSON format.
'''

import json
import requests
from sys import argv

if __name__ == "__main__":
    emp_id = argv[1]
    api_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    response = requests.get(api_url)
    u_name = response.json().get('username')

    todo_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos'
    response = requests.get(todo_url)
    todo_list = response.json()

    Emp_Dict = {emp_id: []}
    for task in todo_list:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = u_name
        Emp_Dict[emp_id].append(task_dict)

    with open("{}.json".format(emp_id), 'w') as json_file:
        json.dump(Emp_Dict, json_file)



