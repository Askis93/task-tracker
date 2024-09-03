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

current_time = datetime.now()
formatted_time = current_time.strftime('%H:%M %d %B %Y')

def add_task():

    tasks = args.add

    if not os.path.exists(task_file):
    # turn task into a dictionary because it's a new json file
        tasks = [
            {
                'id': 1,
                'description': args.add,
                'status': 'todo',
                'createdAt': formatted_time,
                'updatedAt': formatted_time
            }
        ]
        with open(task_file, 'w') as file:
            json.dump(tasks, file, indent=4)
        print(tasks)
    else:
        with open(task_file, "r") as file:
            data = json.load(file)
            
            highest_id = None
            for task in data:
                if highest_id == None:
                    highest_id = task.get("id")
                    continue
                if task.get("id") > highest_id:
                    highest_id = task.get("id")

            new_task = {
                "id" : highest_id + 1,
                "description" : args.add,
                "status": "todo",
                "createdAt" : formatted_time,
                "updatedAt" : formatted_time
            }
            
            data.append(new_task)

            print(json.dumps(data, indent=4))
        
        with open(task_file, "w") as file:
            json.dump(data, file, indent=4)



def delete_task():

    delete_task = args.delete
    task_was_deleted = False
    print("Trying to delete task: " + delete_task)

    with open(task_file, "r") as file:
        data = json.load(file)
        newdata = []
        for obj in data:
            if obj.get('id') != int(delete_task):
                newdata.append(obj)
            else:
                task_was_deleted = True

    if task_was_deleted == False:
        print("No task with that id")
        return
    with open(task_file, "w") as file:
        json.dump(newdata, file, indent=4)

def list_tasks():
    
    filter = args.list
    
    with open(task_file, "r") as file:
        data = json.load(file)
        
        if filter == "all":
            print(json.dumps(data, indent=4))

        if filter == "done":
            tasks_done = []
            for task in data:
                if task.get("status") == "done":
                    tasks_done.append(task)
            print(json.dumps(tasks_done, indent=4))

        if filter == "in-progess":
            tasks_done = []
            for task in data:
                if task.get("status") == "in-progess":
                    tasks_done.append(task)
            print(json.dumps(tasks_done, indent=4))

        if filter == "todo":
            tasks_done = []
            for task in data:
                if task.get("status") == "todo":
                    tasks_done.append(task)
            print(json.dumps(tasks_done, indent=4))
            

def update_task():
    pass

def mark_as_done():
    pass

def mark_as_in_progress():
    pass
    


if args.add:
    add_task()

elif args.list:
    list_tasks()

elif args.delete:
    delete_task()
