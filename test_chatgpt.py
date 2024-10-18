from datetime import datetime
class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = 'Выполнено' if self.completed else 'Не выполнено'
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        new_task = Task(description, due_date)
        self.tasks.append(new_task)
        print(f"Добавлена задача: {description}, Срок: {due_date}")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Задача '{self.tasks[index].description}' выполнена!")
        else:
            print("Некорректный индекс задачи.")

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def show_tasks(self):
        print("Список задач:")
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")


# Пример использования:
manager = TaskManager()
manager.add_task("Купить продукты", "2024-10-20")
manager.add_task("Сделать домашнее задание", "2024-10-21")
manager.show_tasks()

manager.mark_task_completed(0)
print("Текущие задачи:")
for task in manager.get_current_tasks():
    print(task)
