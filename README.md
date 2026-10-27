# Task-tracker

project page url: https://roadmap.sh/projects/task-tracker 

The project was done using VScode. Python code is done in the file task_cli.py. Tasks are stored in the JSON file tasks.json

# Requirements
- Add, Update, and Delete tasks
- Mark a task as in progress
- Mark a task as done
- List all tasks
- List all tasks that are done
- List all tasks that are not done
- List all tasks that are in progress

# Task Properties
- id
- description
- status: todo, in-progress, done
- createdAt
- updatedAt

# Example commands for terminal:
- python task_cli.py add "Buy groceries"
- python task_cli.py update 1 "Buy groceries and cook dinner"
- python task_cli.py delete 1
- python task_cli.py mark-in-progress 1
- python task_cli.py mark-done 1
- python task_cli.py list
- python task_cli.py list done
- python task_cli.py list todo
- python task_cli.py list in-progress
