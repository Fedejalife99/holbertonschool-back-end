#!/usr/bin/python3
"""learning how to consume an api"""

import csv
import json
import requests
import sys


def fuc_to_do(emp_id=0):

    if len(sys.argv) == 1:
        return
    emp_id = int(sys.argv[1])
    emp_id -= 1
    usr = requests.get('https://jsonplaceholder.typicode.com/users')
    usr_content = usr.content
    usr_content_to_json = json.loads(usr_content)
    emp_name = usr_content_to_json[emp_id]['name']
    all_tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    all_tasks_content = all_tasks.content
    all_tasks_content_to_json = json.loads(all_tasks_content)
    list_of_tasks = []
    task_completed = 0
    task_imcompleted = 0
    user_name = usr_content_to_json[emp_id]['username']
    for task_info in all_tasks_content_to_json:
        if task_info['completed'] is True and task_info['userId'] == emp_id:
            list_of_tasks.append(format(task_info['title']))
            task_completed += 1
        if task_info['completed'] is False and task_info['userId'] == emp_id:
            task_imcompleted += 1
    total_tasks = task_completed + task_imcompleted
    s = "Employee {} is done with tasks({}/{}):".format(
        emp_name, task_completed, total_tasks)
    print(s)
    for list in list_of_tasks:
        print('\t', end=" ")
        print(list)
    emp_id += 1
    with open('{}.csv'.format(emp_id),
              'w+', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task_info in all_tasks_content_to_json:
            if task_info['userId'] == emp_id:
                writer.writerow(
                    [str(emp_id), user_name, str(task_info['completed']),
                     task_info['title']])


if __name__ == "__main__":
    fuc_to_do()
