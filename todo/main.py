import datetime
import json
from enum import Enum


# class Dni(Enum):
#     PONIEDZIAŁEK = 1
#     WTOREK = 2
#     ŚRODA = 3
#     CZWARTEK = 4
#     PIĄTEK = 5
#     SOBOTA = 6
#     NIEDZIELA = 7
    
class Zadanie:
    """Klasa, z której powstaną poszczególne zadania"""
    def __init__(self, task_id: int, tytul: str, opis: str, dzien_tygodnia: str = '') -> None:
        self.task_id = task_id
        self.tytul = tytul
        self.opis = opis
        self.dzien_tygodnia = dzien_tygodnia
        
    # def usun(self):
    #     del self
    #     print("Usunięto zadanie")
    # nie działa, del nie usuwa instancji tylko zmienną self
            
    # def print_zadanie(self, flag: bool = False) -> None:
    #     """Wyświetla zadanie, jeżeli została podana flaga, to wyświetla też opis"""
    #     print("Termin zadania:", Dni(self.termin).name)
    #     print("Tytuł zadania:", self.tytul)
    #     print("ID zadania:", self.id)
    #     if(flag):
    #         print("Opis:", self.opis)
    #     else:
    #         pass
    
        
class TodoList:
    """Główna klasa listy todo"""
    def __init__(self):
        self.tasks = []

    def dodaj_zadanie(self, tytul: str, opis: str, dzien_tygodnia: str) -> None:
        task_id = len(self.tasks) + 1
        task = Zadanie(task_id, tytul, opis, dzien_tygodnia)
        self.tasks.append(task)

    def usun_task(self, task_id: int) -> None:
        """Szuka zadania i usuwa je zgodnie z podanym id"""
        task = self.znajdz_zadanie_id(task_id)
        if task:
            self.tasks.remove(task)
            print("Zadanie usunięte")
        else:
            print("Brak zadania o tym id")

    def update_task(self, task_id: int, new_tytul=None, new_opis=None, new_dzien_tygodnia=None) -> None:
        """Szuka zadania za pomocą id i pozwala zmienić detale o ile zostały podane"""
        task = self.znajdz_zadanie_id(task_id)
        if task:
            if new_tytul:
                task.tytul = new_tytul
            if new_opis:
                task.opis = new_opis
            if new_dzien_tygodnia:
                task.dzien_tygodnia = new_dzien_tygodnia

    def znajdz_zadanie_id(self, task_id: int) -> Zadanie | None:
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def zadanie_wedlug_dnia(self, dzien_tygodnia: str) -> list:
        tasks = []
        for task in self.tasks:
            if task.dzien_tygodnia == dzien_tygodnia:
                tasks.append(task)
        return tasks

    def get_all_tasks(self) -> list:
        return self.tasks

    def save_to_file(self, filename) -> None:
        dane_zadania = []
        for task in self.tasks:
            dane_zadanie = {
                'task_id': task.task_id,
                'tytul': task.tytul,
                'opis': task.opis,
                'dzien_tygodnia': task.dzien_tygodnia
            }
            dane_zadania.append(dane_zadanie)
        with open(filename, 'w') as file:
            json.dump(dane_zadania, file)

    def load_from_file(self, filename) -> None:
        try:
            with open(filename, 'r') as file:
                file_content = file.read()
                if file_content:
                    tasks_data = json.loads(file_content)
                    for task_data in tasks_data:
                        task = Zadanie(
                            task_data['task_id'],
                            task_data['tytul'],
                            task_data['opis'],
                            task_data['dzien_tygodnia'],
                        )
                        self.tasks.append(task)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
        
def print_menu() -> None:
    print("===== TODO LIST =====")
    print("1. Dodaj nowe zadanie")
    print("2. Wyświetl zadania z danego dnia tygodnia")
    print("3. Wyświetl zadania z całego tygodnia")
    print("4. Usuń zadanie")
    print("5. Aktualizuj zadanie")
    print("6. Zapisz zadania do pliku")
    print("7. Wyjdź z programu")

def wybor_fukcjonalnosci(choice: int, todoInstancja: TodoList) -> bool:
    """Przyjmuje wybór funkcjonalności i instancje Todo, by wywoływać odpowiednie funkcje"""
    
    dni_tyg = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
    if choice == 1:
        tytul = input("Podaj tytuł zadania: ")
        opis = input("Podaj opis zadania: ")
        dzien_tygodnia = input("Podaj dzień tygodnia (opcjonalnie): ").lower()
        if dzien_tygodnia in dni_tyg:
            todoInstancja.dodaj_zadanie(tytul, opis, dzien_tygodnia)
            print("Zadanie dodane.")
        else: 
            print("Niepoprawny dzień tygodnia")

        return True
    
    elif choice == 2:
        dzien_tygodnia = input("Podaj dzień tygodnia, z którego chcesz wyświetlić zadania: ").lower()
        if dzien_tygodnia in dni_tyg:
            tasks = todoInstancja.zadanie_wedlug_dnia(dzien_tygodnia)
            if tasks:
                for task in tasks:
                    print(f"ID: {task.task_id}, Tytuł: {task.tytul}, Termin wykonania: {task.dzien_tygodnia}")
            else:
                print("Brak zadań na podany dzień tygodnia.")
        else:
            print("Podano nieprawidłowy dzień tygodnia")
        return True
    
    elif choice == 3:
        all_tasks = todoInstancja.get_all_tasks()
        flaga = True if input("Wyświetlić opis zadania? y/n ") == 'y' else False 
        if all_tasks:
            for task in all_tasks:
                if(flaga):
                    print(f"ID: {task.task_id}, Opis: {task.opis}, Tytuł: {task.tytul}, Termin wykonania: {task.dzien_tygodnia}")
                else:
                    print(f"ID: {task.task_id}, Tytuł: {task.tytul}, Termin wykonania: {task.dzien_tygodnia}")
        else:
            print("Brak zapisanych zadań.")
        return True

    elif choice == 4:
        if(len(todoInstancja.tasks) != 0):
            task_id = int(input("Podaj ID zadania do usunięcia: "))
            todoInstancja.usun_task(task_id)
        else:
            print("Brak zadań do usunięcia")
        
        return True    

    elif choice == 5:
        
        if(len(todoInstancja.tasks) != 0):
            task_id = int(input("Podaj ID zadania do aktualizacji: "))
            new_tytul = input("Podaj nowy tytuł (opcjonalnie): ")
            new_opis = input("Podaj nowy opis (opcjonalnie): ")
            new_dzien_tygodnia = input("Podaj nowy dzień tygodnia (opcjonalnie): ").lower()
            
            if new_dzien_tygodnia:    
                
                if new_dzien_tygodnia in dni_tyg:
                    todoInstancja.update_task(task_id, new_tytul, new_opis, new_dzien_tygodnia)
                    print("Zadanie zaktualizowane.")
                    return True
                
                elif new_dzien_tygodnia not in dni_tyg:
                    print("Niepoprawny dzień tygodnia")
                    return True
                
            todoInstancja.update_task(task_id, new_tytul, new_opis)
            print("Zadanie zaktualizowane.")
            return True
        
        else:
            print("Brak zadań do aktualizacji")
            return True
        
    elif choice == 6:
        filename = 'zadania.json'
        todoInstancja.save_to_file(filename)
        print("Zadania zapisane do pliku.")
        return True

    elif choice == 7:
        return False

    else:
        print("Nieprawidłowa opcja. Spróbuj ponownie.")
        return True

def main():
    flag = True
    todo = TodoList()
    todo.load_from_file('zadania.json')
    while flag:
        print_menu()
        try:
            choice = int(input("Wybierz opcję: "))
        except ValueError:
            print("Niepoprawny wybór")
            continue
        flag = wybor_fukcjonalnosci(choice, todo)
        
    print("System autodestrukcji został aktywowany!")

main()

# class User:
#     id: int = -1
#     def __init__(self) -> None:
#         self.id = User.id + 1
#         self.listaZadan = []
        
#     def setListaZadan(self, zadanie: Zadanie) -> None:
#         self.listaZadan.append(zadanie)
#         print("New current book set")
        
# def get_user_choice() -> int:
#     """Funkcja, która pobiera od użytkownika liczbę (numer wybranej podfunkcji) i zwraca ją w miejscu wywołania"""
#     return int(input("Wybierz operację za pomocą odpowiedniej liczby: "))

# def print_info() -> None:
#     """Funkcja odpowiedzialna za wyświetlenie informacji - dostępnych funkcji todo"""
#     print("""Dostępne funkcje to:
#           \n1. Wyświetl zadania
#           \n2. Usuń zadanie
#           \n3. Aktualizuj zadanie
#           \n0. Wyjdź
#           """)
    
# listaZadan: list[Zadanie] = []   

# def main() -> None:
#     """Główna pętla todo"""
#     while True:
#         print_info()
#         try:
#             operacja = get_user_choice()
#         except ValueError:
#             print("Niepoprawny wybór")
#             continue
#         if operacja <= 0 or operacja > 3:
#             print("Wybrana opcja nie istnieje, spróbuj ponownie")
#             continue
#         else:
#             pass


# # Choose = input('Wybierz dzień').upper()

# # print(type(getattr(Dni, Choose).name))

# # print(Dni['WT'].value)
# # print(Dni(1).name)

# z = Zadanie('Test', 'test', 'WTOREK')
# z.print_zadanie()
# z.usun()
# print(z)