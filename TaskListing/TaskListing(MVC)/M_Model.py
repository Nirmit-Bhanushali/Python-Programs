class TaskModel:
    # the Model manages the data and state of the application
    # if doesn't care how the data is displayed or how user input is handled.
    def __init__(self):
        # The internal state(data)
        self.tasks = []
    def get_all_tasks(self):
        # Business logic: return a copy of the tasks
        return list(self.tasks)
    def add_task(self, task_name):
        # Business logic: validate and add new data
        if not task_name or len(task_name.strip())<3:
            raise ValueError("Task name must be at least 3 characters long.")
        # Store data as a simple dictionary
        self.tasks.append({
            "name":task_name.strip(),
            "done":False
        })
        return True
    def mark_task_done(self,index):
        # Marks a task as done based on its 0-based index
        if 0<=index <len(self.tasks):
            self.tasks[index]["done"]=True
            return True
        return False