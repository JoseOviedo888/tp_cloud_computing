def add_task(tasks, title):
    tasks.append({"title": title, "completed": False})

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True

def get_tasks(tasks):
    return tasks
