from enum import Enum

class Book:
    def __init__(self) -> None:
        self.nazwa = "Testowa książka"

class Sex(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    
class Czytelnik:
    id: int = -1
    
    def __init__(self, firstname: str, surname: str, year_of_birth: int, sex: Sex, books_read: int, current_book: Book) -> None:
        self.id += Czytelnik.id
        self.fullname = self.create_fullname(firstname, surname)
        self.year_of_birth = year_of_birth
        self.sex = sex.name
        self.books_read = books_read
        self.current_book = current_book.nazwa
        
    def create_fullname(self, imie: str, nazwisko: str) -> dict[str, str]:
        return {"first_name": imie, "surname": nazwisko}
    
    # def print_data(self) -> None:
    #     print("Pełne imię: " + self.fullname['first_name'] + ' ' + self.fullname['surname'], "Data urodzenia: " + self.year_of_birth)
    
test_book = Book()

czyt1 = Czytelnik('Konrad', 'Zuzaniuk', 1996, Sex.MALE, 10, test_book)
print(czyt1.current_book)
print(czyt1.sex)

czyt2 = Czytelnik('ADGdga', 'ASDGdag', 1777, Sex.MALE, 5, test_book)
czyt3 = Czytelnik('DGAdag', 'dadADA', 1969, Sex.FEMALE, 3, test_book)