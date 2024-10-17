class Task():

    def __init__(self, name_task, deadline, status):
        self.name_task = name_task
        self.deadline = deadline
        self.status = status

    def add_task(self, task, list_task):
        self.task = task
        self.list_task = list_task
        