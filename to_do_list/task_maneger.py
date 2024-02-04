# === === === ====== === === ====== === === ====== === === ====== === === ====== === === ====== === === ====== === === ====== === === ===
#                                                       To do list program
# Descripion: task maneger for ubuntu.                                                      programer: Lucas Queiroz.
# === === === ====== === === ====== === === ====== === === ====== === === ====== === === ====== === === ====== === === ====== === === ===

# Imports
import argparse
import json
from datetime import datetime


# maneger for the tasks:
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    # Load the tasks from the .json file.
    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            pass

    # Write the tasht in the .json file
    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file, indent=2)

    # display the taks in the terminal.
    def display_tasks(self):
        print('=== Lista de Tarefas ===')
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task['description']} - {task['due_date']}")
        print('=======================')

    # adding a new task to the .json file.
    def add_task(self, description, due_date):
        new_task = {'description': description, 'due_date': due_date}
        self.tasks.append(new_task)
        self.save_tasks()
        print(f'Tarefa adicionada: {description}')


def perser_argmumets():
    parser = argparse.ArgumentParser(prog='taskM', description='A taks maneger')
    parser.add_argument(
        '--add',
        nargs=2,
        metavar=('[DESCRIPTION]', ',[DATE]'),
        help='Add a new task.',
    )
    parser.add_argument('--list', action='store_true', help='list all tasks.')
    return parser.parse_args()


# displaying every thing in the terminal
if __name__ == '__main__':
    task_manager = TaskManager()

    args = perser_argmumets()

    if args.add:
        description, due_date = args.add
        task_manager.add_task(description, due_date)
    elif args.list:
        task_manager.display_tasks()
