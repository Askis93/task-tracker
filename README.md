# Task Tracker

Task Tracker is a simple command-line application that allows you to add, update, mark, and delete tasks in a JSON file. The application also lets you view a list of tasks based on their status.

## Features

- **Add Task**: Add a new task with a given description.
- **List Tasks**: View a list of tasks based on their status (all, todo, in progress, or done). Default is to show all.
- **Update Task Description**: Update the description of an existing task based on its ID.
- **Mark Task Status**: Change the status of a task to "in progress" or "done" based on its ID.
- **Delete Task**: Remove an existing task based on its ID.

## Usage

### Add Task

To add a new task, use the `-a` or `--add` argument:

```bash
python task_tracker.py -a "Create a new task"
```

### List Tasks

To list tasks based on their status, use the `-l` or `--list` argument. You can specify "todo", "in progress", "done", or "all" (all are shown if not specified):

```bash
python3 task_tracker.py -l "in progress"
```

### Update Task Description

Update the task description by using `-p` to pick a specific task and the `-u` to change the description.

```bash
python3 task_tracker.py -p 2 -u "Updated Task Description"
```

### Mark Task Status

Mark a task as "in progress" or "done", use the `-p` to pick a specific task and then either `--done` or `--progress` argument to provide the new status:

```bash
python3 task_tracker.py -p 2 --progress
```

### Delete Task

Delete a task by using `-p` to pick a specific task and the `-d` to delete it:

```bash
python3 task_tracker.py -p 2 -d
```

## Notes

- Ensure that the `tasks.json` file exists in the same directory as the script for it to function correctly.
- The application will create the `tasks.json` file if it does not already exist when adding a new task.

## Project Link

For more details about this project, visit the [Task Tracker Project Roadmap](https://roadmap.sh/projects/task-tracker).