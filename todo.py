import os

# Menu action
add = 1
edit = 2
done = 3
delete = 4
list_task = 5
closse = 6
min_option = 1
max_option = 6

class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.done = "Programado"

    def print_data(self, index):
        print(f"{index}. TAREA: {self.name}") 
        print(f"   Fecha {self.due_date}")
        print(f"   Estado: {self.done}")

def print_menu():
    print("**************************")
    print("*     T U T A N K A      *")
    print("*       T O - D O        *")
    print("**************************")
    print("*Seleccione una opcioón  *")
    print("**************************")
    print("* 1. Agregar tarea")
    print("* 2. Editar tarea")
    print("* 3. Marcar como hecha")
    print("* 4. Borrar tarea")
    print("* 5. Listar tarea")
    print("* 6. Salir")

def print_title_list():
    print("**************************")
    print("     LISTADO DE TAREAS")
    print("**************************")
    print()

def validate_option(option):
    if option < min_option or option > max_option:
        return False
    return True

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

def process_add_task(to_do):
    print("1. CREAR TAREA")
    task = create_task()
    add_task(task, to_do)
    print("Tarea creada")

def print_all_task(to_do):
    index = 0
    for task in to_do:
        index += 1
        task.print_data(index)

def get_index():
    try:
        index = int(input("Digite el número de la tarea: "))
    except ValueError:
        print("Número no válido")
    return index

def edit_task(index, new_task, to_do):
    to_do[index - 1] = new_task

def process_edit_task(to_do):
    print("2. EDITAR TAREA")
    index = get_index()
    task = create_task()
    edit_task(index, task, to_do)
    print("Tarea editada correctamente")

def set_is_done():
    value = input("Digite 1 si se realizo, de lo contrario cualquier tecla: ")
    if value == '1':
        return "Hecho"
    
    return "Programdo"

def done_task(index, done, to_do):
    to_do[index - 1].done = done

def process_done_task(to_do):
    print("3. MARCAR COMO HECHO")
    index = get_index()
    done = set_is_done()
    done_task(index, done, to_do)

def delete_task(index, to_do):
    del to_do[index - 1]

def process_delete_task(to_do):
    print("4. BORRAR TAREA")
    index = get_index()
    delete_task(index, to_do)
    print("Tarea borrada")

def process(option, to_do):
    os.system("cls") # Clear console for Windows "cls", for Linux use "clear" 
    if option == add:
        process_add_task(to_do)
        return
    elif option == edit:
        process_edit_task(to_do)
        return
    elif option == done:
        process_done_task(to_do)
        return
    elif option == delete:
        process_delete_task(to_do)
        return
    elif option == list_task:
        print_title_list()
        print_all_task(to_do)
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
        process(option, to_do)

if __name__ == '__main__':
    run()