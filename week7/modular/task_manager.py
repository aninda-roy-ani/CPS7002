from task import Task
from user import User


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.users = []

    def add_task(self, title, description, assigned_to):
        task = Task(title, description, assigned_to)
        self.tasks.append(task)

    def assign_task(self, task_title, user_name):
        for task in self.tasks:
            if task.title == task_title:
                task.assigned_to = user_name
                task.status = "Assigned"
                break

    def complete_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.status = "Completed"
                break

    def display_tasks(self):
        for task in self.tasks:
            task.display()

    def add_user(self, name):
        self.users.append(User(name))