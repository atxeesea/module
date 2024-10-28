TaskList = []

def add_task(task):
    return TaskList.append(task)

def mark_complete(task):
    if task in TaskList:
        TaskList.remove(task)
        TaskList.append(f'[ok] {task}')
    else:
        return 'Задачи нет в списке'
    
def view_list():
    return TaskList

def clear_list():
    return TaskList.clear()
