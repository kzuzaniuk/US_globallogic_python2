from abc import ABC, abstractmethod

class What(ABC):
    
    def __init__(self) -> None:
        # super().__init__()
        
    @abstractmethod
    def abstrakcyjna_metoda(self):
        pass