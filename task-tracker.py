import json
import argparse
import os
from datetime import datetime

# Create parser
parser = argparse.ArgumentParser()

# Parse arguments
parser.add_argument("-a", "--add", help="Add task to tracker", required=False)
parser.add_argument("-l", "--list", help="Show tasks, filter by [all, done, todo, in progress]", const="all", nargs="?", required=False)
parser.add_argument("-u", "--update", help="Type new description", required=False)
parser.add_argument("-p", "--pick", help="Task id", required=False)
parser.add_argument("-d", "--delete", help="Delete task", required=False, action="store_true")
parser.add_argument("--done", help="Mark as done", required=False, action="store_true")
parser.add_argument("--progress", help="Mark as in progress", required=False, action="store_true")

# Process arguments
args = parser.parse_args()

# File path
task_file = "tasks.json"

# Create and format time to dd-mm-yy HH:MM
current_time = datetime.now()
formatted_time = current_time.strftime('%H:%M %d %B %Y')

# Add new task
def add_task():
    tasks = args.add

    if not os.path.exists(task_file):
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

# Delete existing task
def delete_task():
    delete_task = args.pick
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
        print("Task " + delete_task + " was deleted")

# List tasks based on given filter option
def list_tasks():
    filter = args.list
    
    with open(task_file, "r") as file:
        data = json.load(file)
        
        tasks_done = []
        if filter == "all":
            print(json.dumps(data, indent=4))

        elif filter == "done":
            for task in data:
                if task.get("status") == "done":
                    tasks_done.append(task)
            print(json.dumps(tasks_done, indent=4))

        elif filter == "in progress":
            for task in data:
                if task.get("status") == "in progress":
                    tasks_done.append(task)
            print(json.dumps(tasks_done, indent=4))

        elif filter == "todo":
            for task in data:
                if task.get("status") == "todo":
                    tasks_done.append(task)
            print(json.dumps(tasks_done, indent=4))
            
# Update specified tasks description
def update_task():
    task_id = args.pick
    update_task = args.update

    with open(task_file, "r") as file:
        data = json.load(file)

        task_found = False
        for task in data:
            if task.get("id") == int(task_id):
                task["description"] = update_task
                task["updatedAt"] = formatted_time
                task_found = True
                break

        if task_found == True:
            with open(task_file, "w") as file:
                json.dump(data, file, indent=4)

    print("Task " + task_id + " was updated with description: " + update_task)

# Update specified tasks status
def mark_status():
    task_id = args.pick

    with open(task_file, "r") as file:
        data = json.load(file)

        task_found = False
        for task in data:
            if task.get("id") == int(task_id):
                if args.done:
                    task["status"] = "done"
                    print("Task " + task_id + " is now status: done")
                else:
                    task["status"] = "in progress"
                    print("Task " + task_id + " is now status: in-progress")
                task_found = True
                task["updatedAt"] = formatted_time

        if task_found == True:
            with open(task_file, "w") as file:
                json.dump(data, file, indent=4)


if args.add:
    add_task()

elif args.list:
    list_tasks()

elif args.pick:
    if args.delete:
        delete_task()
    elif args.update:
        update_task()
    elif args.done or args.progress:
        mark_status()
    else:
        parser.error("When using 'pick', --delete, --update, --done, or --progress must be specified")

else:
    exit()
