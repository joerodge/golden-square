class TaskFormatter:
    def __init__(self, task): # task is an instance of Task
        self.task = task

    def format(self):
        # Returns the task formatted as a string.
        # If the task is not complete, the format is:
        # - [ ] Task title
        # If the task is complete, the format is:
        # - [x] Task title
        cross = 'x' if self.task.is_complete() else ' '
        return f"- [{cross}] {self.task.title}"

class Task:
    def __init__(self, title):
        self.title = title
        self.complete = False

    def mark_complete(self):
        self.complete = True

    def is_complete(self):
        return self.complete
    


