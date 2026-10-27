import json
import sys
import os
from datetime import datetime


TASKS_FILE = "tasks.json"

# FILE HANDLING
# try, except are error handling, if file is not found, it will return an empty list
def load_tasks():
    try:
        with open(TASKS_FILE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):  #covers no file, empty file, and invalid JSON
        return []

def save_tasks(tasks):
    """Write the list of tasks to the JSON file."""
    json_str = json.dumps(tasks, indent=4)   # converts dictionary to a JSON object and formats it with indentation for readability
    with open(TASKS_FILE, "w") as f:
        f.write(json_str)


# COMMANDS
def add(description):
    tasks = load_tasks()
    new_id = max((t["id"] for t in tasks), default = 0) + 1 #finds the largest id in tasks and adds 1 to it, if no tasks exist, it will default to 0
    now = datetime.now().isoformat()  #gives a datetime object in ISO 8601 format, which is a standard format for representing date and time
    
    
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "created_at": now,
        "updated_at": now,
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id}): '{description}'")
    
    
def update(id, description):
    found = False
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            found = True
            old_description = task["description"]
            task["description"] = description
            task["updated_at"] = datetime.now().isoformat()
            print(f"Task updated successfully (ID: {id}) from '{old_description}' to '{description}'")
    if not found:
        print(f"No task found with ID: {id}")
    save_tasks(tasks)

def delete(id):
    found = False
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            found = True
            description = task["description"]
            tasks.remove(task)
            print(f"Task deleted successfully (ID: {id}): '{description}'")
    if not found:
        print(f"No task found with ID: {id}")
    save_tasks(tasks)


def mark_in_progress(id):
    found = False
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            found = True
            task["status"] = "in-progress"
            task["updated_at"] = datetime.now().isoformat()
            print(f"Task marked as in-progress successfully (ID: {id}): '{task['description']}'")
    if not found:
        print(f"No task found with ID: {id}")
    save_tasks(tasks)

def mark_done(id):
    found = False
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            found = True
            task["status"] = "done"
            task["updated_at"] = datetime.now().isoformat()
            print(f"Task marked as done successfully (ID: {id}): '{task['description']}'")
    if not found:
        print(f"No task found with ID: {id}")
    save_tasks(tasks)
    

def list(status_filter=None):
    tasks = load_tasks()
    chosen = []
    if status_filter is None:
        chosen = tasks
    else:
        for task in tasks:
            if task["status"] == status_filter:
                chosen.append(task)
    
    # print the chosen tasks
    if chosen:
        for task in chosen:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['created_at']}, Updated At: {task['updated_at']}")
    elif status_filter == "todo":
        print("No tasks found with status 'todo'.")
    elif status_filter == "in-progress":
        print("No tasks found with status 'in-progress'.")  
    elif status_filter == "done":
        print("No tasks found with status 'done'.")
    else:
        print(f"{status_filter} is not a valid status. Valid statuses are: todo, in-progress, done.")

# entry point, running the code

def main():
    # 1. Read sys.argv
    print("Command-line arguments:", sys.argv)
    # 2. Check that a command was given
    if len(sys.argv) < 2:
        print("Please provide a command.")
        return 
    # 3. Decide which function to call based on the command
    if len(sys.argv) >= 2:
        command = sys.argv[1]
        if command == "add":
            if len(sys.argv) < 3:
                print("Please provide a description for the task.")
                return
            description = " ".join(sys.argv[2:])
            add(description)
        elif command == "update":
            if len(sys.argv) < 4:
                print("Please provide an ID and a new description for the task.")
                return
            try:
                id = int(sys.argv[2])
            except ValueError:
                print("ID must be an integer.")
                return
            description = " ".join(sys.argv[3:])
            update(id, description)
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Please provide an ID for the task to delete.")
                return
            try:
                id = int(sys.argv[2])
            except ValueError:
                print("ID must be an integer.")
                return
            delete(id)
        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Please provide an ID for the task to mark as in progress.")
                return
            try:
                id = int(sys.argv[2])
            except ValueError:
                print("ID must be an integer.")
                return
            mark_in_progress(id)
        elif command == "mark-done":
            if len(sys.argv) < 3:
                print("Please provide an ID for the task to mark as done.")
                return
            try:
                id = int(sys.argv[2])
            except ValueError:
                print("ID must be an integer.")
                return
            mark_done(id)
        elif command == "list":
            status_filter = sys.argv[2] if len(sys.argv) > 2 else None
            list(status_filter)
        else:
            print(f"Unknown command: {command}")
    # 4. Pass it the remaining arguments
    


if __name__ == "__main__":
    main()