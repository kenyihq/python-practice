# Menu action
add = 1
edit = 2
done = 3
delete = 4
list_task = 5
closse = 6
min_option = 1
max_option = 2


class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.done = False

    def print_data(self, index):
        print(f"{index}. Tarea: {self.name}, Fecha {self.due_date}, Hecha {self.done}")

def print_menu():
    print("************************")
    print("*        T O D O       *")
    print("************************")
    print("Seleccione una opcioón *")
    print("************************")
    print("* 1. Agregar tarea")
    print("* 2. Editar tarea")
    print("* 3. Marcar como hecha")
    print("* 4. Borrar tarea")
    print("* 5. Listar tarea")
    print("* 6. Salir")

def print_title_list():
    print()
    print("************************")
    print("LISTADO DE TAREAS")
    print("************************")
    print()

def validate_option(option):
    if option < min_option or option > max_option:
        return False

def get_option():
    try:
        option = int(input("Digite la opción: "))        
        return option
    except ValueError:
        print("\nDigite una opción válida")
        return False

def create_task():
    name = input("Nombre: ")
    due_date = input("Fecha: ")
    task = Task(name, due_date)
    return task

def new_list():
    return []

def add_task(task, to_do):
    to_do.append(task)

def process(option, to_do):
    if option == add:
        print("1. CREAR TAREA")
        task = create_task()
        return
    elif option == edit:
        print("2. Funcion no implementada aún")
        return
    elif option == done:
        print("3. Funcion no implementada aún")
        return
    elif option == delete:
        print("4. Funcion no implementada aún")
        return
    elif option == list_task:
        print("5. Funcion no implementada aún")
        return


def run():
    option = 0
    to_do = new_list()
    while option != closse:
        print_menu()
        option = get_option()
        if not validate_option(option):
            print("Solo digite del 1 al 6")
            continue
        process(option)
if __name__ == '__main__':
    run()