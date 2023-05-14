from enum import Enum

class Book:
    def __init__(self, nazwa: str) -> None:
        self.nazwa = nazwa

class Sex(Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'
    
class Czytelnik:
    id: int = -1
    
    def __init__(self, firstname: str, surname: str, year_of_birth: int, sex: Sex, books_read: int, current_book: Book) -> None:
        Czytelnik.id += 1
        self.__id = Czytelnik.id
        self.__fullname = self.create_fullname(firstname, surname)
        self.__year_of_birth = year_of_birth
        self.__sex = sex.value
        self.__books_read = books_read
        self.__current_book = current_book.nazwa
        
    def create_fullname(self, imie: str, nazwisko: str) -> dict[str, str]:
        return {"first_name": imie, "surname": nazwisko}
    
    def set_current_book(self, new_book: Book) -> None:
        self.__current_book = new_book.nazwa
        print("New current book set")
        
    def set_books_read(self, ammount: int) -> None:
        self.__books_read = ammount
        
    def get_current_book_name(self) -> str:
        return self.__current_book
    
    def get_books_read(self) -> int:
        return self.__books_read
    
    def get_fullname(self) -> dict[str, str]:
        return self.__fullname
    
    def get_id(self) -> int:
        return self.__id
    
    def get_year_of_birth(self) -> int:
        return self.__year_of_birth
    
    def get_sex(self) -> str:
        return self.__sex
    # def print_data(self) -> None:
    #     print("Pełne imię: " + self.fullname['first_name'] + ' ' + self.fullname['surname'], "Data urodzenia: " + self.year_of_birth)
    
test_book = Book('Testowa książka 1')

test_book2 = Book('Testowa książka 2')

czyt1 = Czytelnik('Konrad', 'Zuzaniuk', 1996, Sex.MALE, 10, test_book)

czyt2 = Czytelnik('ADGdga', 'ASDGdag', 1777, Sex.MALE, 5, test_book)
czyt3 = Czytelnik('DGAdag', 'dadADA', 1969, Sex.FEMALE, 3, test_book)

czyt3.set_current_book(test_book2)
print(czyt3.get_current_book_name())

print("Czytelnik 2 id: ", czyt2.get_id(), sep="")