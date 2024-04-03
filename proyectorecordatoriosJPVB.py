from datetime import datetime

# Patrón Singleton para el Gestor de Tareas
class TaskManagerSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.tasks = []
        return cls._instance

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task_index):
        if task_index >= 0 and task_index < len(self.tasks):
            self.tasks[task_index].completed = True
        else:
            print("Índice de tarea inválido.")

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]


# Patrón Strategy para mostrar las tareas
class TaskDisplayStrategy:
    def display(self, tasks):
        raise NotImplementedError("Subclasses must implement display method.")


class ConsoleTaskDisplayStrategy(TaskDisplayStrategy):
    def display(self, tasks):
        if tasks:
            print("+--------+--------------+------------------------+-----------------------+-----------------------------+------------+")
            print("| Código |  Prioridad   |       Categoría        |         Título        |         Descripción         |   Estado   |")
            print("+--------+--------------+------------------------+-----------------------+-----------------------------+------------+")
            for i, task in enumerate(tasks, start=1):
                title_lines = [task.title[i:i+20] for i in range(0, len(task.title), 20)]
                description_lines = [task.description[i:i+25] for i in range(0, len(task.description), 25)]
                for j in range(max(len(title_lines), len(description_lines))):
                    title = title_lines[j] if j < len(title_lines) else ""
                    description = description_lines[j] if j < len(description_lines) else ""
                    estado = "Pendiente" if not task.completed else "Completada"
                    if j == 0:
                        print(f"| {str(i).ljust(6)} | {task.priority.capitalize().ljust(12)} | {task.category.capitalize().ljust(22)} | {title.ljust(21)} | {description.ljust(27)} | {estado.ljust(10)} |")
                    else:
                        print(f"| {''.ljust(6)} | {''.ljust(12)} | {''.ljust(22)} | {title.ljust(21)} | {description.ljust(27)} | {''.ljust(10)} |")
            print("+--------+--------------+------------------------+-----------------------+-----------------------------+------------+")
        else:
            print("No hay tareas pendientes.")


# Clase Tarea
class Task:
    def __init__(self, title, description, due_date, priority, category):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.priority = priority
        self.category = category


# Función para mostrar el menú
def mostrar_menu():
    print("----- MENÚ -----")
    print("1. Agregar tarea")
    print("2. Completar tarea")
    print("3. Mostrar tareas pendientes")
    print("4. Mostrar tareas completadas")
    print("5. Cambiar estado de tarea")
    print("6. Salir")


# Función para mostrar las tareas
def mostrar_tareas(strategy, tasks):
    strategy.display(tasks)


if __name__ == "__main__":
    # Crear instancia del Gestor de Tareas (Singleton)
    task_manager = TaskManagerSingleton()

    # Estrategia para mostrar tareas en la consola
    console_display_strategy = ConsoleTaskDisplayStrategy()

    # Opciones de prioridad y categoría
    prioridades = {"1": "Baja", "2": "Media", "3": "Alta"}
    categorias = {"1": "Personal", "2": "Academica", "3": "Laboral", "4": "Otras"}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            title = input("Ingrese el título de la tarea: ")
            description = input("Ingrese la descripción de la tarea: ")

            print("Seleccione la prioridad:")
            for key, value in prioridades.items():
                print(f"{key}. {value}")
            priority_input = input("Opción: ")
            priority = prioridades.get(priority_input)
            while priority is None:
                print("Opción de prioridad inválida.")
                priority_input = input("Opción: ")
                priority = prioridades.get(priority_input)

            print("Seleccione la categoría:")
            for key, value in categorias.items():
                print(f"{key}. {value}")
            category_input = input("Opción: ")
            category = categorias.get(category_input)
            while category is None:
                print("Opción de categoría inválida.")
                category_input = input("Opción: ")
                category = categorias.get(category_input)

            while True:
                due_date_input = input("Ingrese la fecha y hora de vencimiento de la tarea (YYYY-MM-DD HH:MM): ")
                try:
                    due_date = datetime.strptime(due_date_input, "%Y-%m-%d %H:%M")
                    break
                except ValueError:
                    print("Formato de fecha y hora inválido. Por favor, ingrese la fecha y hora en el formato correcto (YYYY-MM-DD HH:MM:SS).")
            task_manager.add_task(Task(title, description, due_date, priority, category))
            print("Tarea agregada exitosamente.")

        elif opcion == "2":
            tasks_pending = task_manager.get_pending_tasks()
            if tasks_pending:
                print("Tareas pendientes:")
                mostrar_tareas(console_display_strategy, tasks_pending)
                task_index = int(input("Seleccione el número de la tarea que desea completar: ")) - 1
                task_manager.complete_task(task_index)
                print("Tarea completada exitosamente.")
            else:
                print("No hay tareas pendientes para completar.")

        elif opcion == "3":
            tasks_pending = task_manager.get_pending_tasks()
            print("Tareas pendientes:")
            mostrar_tareas(console_display_strategy, tasks_pending)

        elif opcion == "4":
            tasks_completed = task_manager.get_completed_tasks()
            print("Tareas completadas:")
            mostrar_tareas(console_display_strategy, tasks_completed)

        elif opcion == "5":
            tasks = task_manager.get_pending_tasks()
            if tasks:
                print("Tareas pendientes:")
                mostrar_tareas(console_display_strategy, tasks)
                task_index = int(input("Seleccione el número de la tarea que desea cambiar de estado: ")) - 1
                task_manager.complete_task(task_index)
                print("Estado de tarea cambiado exitosamente.")
            else:
                print("No hay tareas pendientes para cambiar de estado.")

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")