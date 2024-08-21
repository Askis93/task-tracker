import json
import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--add", help="Add task to tracker", required=False)
parser.add_argument("-l", "--list", help="Show tasks, filter by [all, done, todo, in-progress]", const="all", nargs="?", required=False)
parser.add_argument("-u", "--update", help="Update task", required=False)
parser.add_argument("-d", "--delete", help="Delete task", required=False)
parser.add_argument("-c", "--complete", help="Mark as done", required=False)
parser.add_argument("-p", "--progress", help="Mark as in progress", required=False)

args = parser.parse_args()

task_file = "tasks.json"

def add_task():

    tasks = args.add

    print("Add task: " + tasks)

    with open(task_file, "r") as file:
        data = json.load(file)
        print(json.dumps(data))

def delete_task():
    print("Delete task")

def list_tasks(status):
    
    filter = args.list
    
    with open(task_file, "r") as file:
        data = json.load(file)
        
        if filter == "all":
            print(json.dumps(data))

def update_task():
    pass

def mark_as_done():
    pass

def mark_as_in_progress():
    pass
    


if args.add:
    add_task()

elif args.list:
    list_tasks(str(args.list))
