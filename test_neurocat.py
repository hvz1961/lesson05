class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        new_task = Task(description, deadline)
        self.tasks.append(new_task)

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
        else:
            print("Некорректный индекс задачи!")

    def list_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if not current_tasks:
            print("Нет текущих задач.")
        else:
            for index, task in enumerate(current_tasks):
                print(f"{index}. {task}")


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Купить продукты", "2023-10-15")
    manager.add_task("Закончить проект", "2023-10-20")
    manager.add_task("Сделать домашку", "2023-10-18")

    print("Текущие задачи:")
    manager.list_current_tasks()

    print("\nОтмечаем первую задачу как выполненную...")
    manager.mark_task_completed(0)

    print("\nОбновленный список текущих задач:")
    manager.list_current_tasks()
