from abc import ABC, abstractmethod

class Figura(ABC):
    
    def __init__(self, nazwa: str = 'figura') -> None:
        self.nazwa = nazwa
        pass
    
    @abstractmethod
    def poleFigury(self):
        pass
    
    @abstractmethod
    def obwódFigury(self):
        pass
    
    
class CzworokatRowneBoki(Figura):
    
    def __init__(self, nazwa: str = 'kwadrat', bok: float = 1) -> None:
        super().__init__(nazwa)
        self.bok = bok
        
    def poleFigury(self) -> float:
        return self.bok**2
    
    def obwódFigury(self) -> float:
        return self.bok*4
    
class Prostokat(Figura):
    
    def __init__(self, nazwa: str = 'prostokąt', bok: float = 1, bok2: float = 1) -> None:
        super().__init__(nazwa)
        self.bok = bok
        self.bok2 = bok2
        
    def poleFigury(self) -> float:
        return self.bok*self.bok2
    
    def obwódFigury(self) -> float:
        return 2*self.bok + 2*self.bok2
    
class Trapez(Figura):
    
    def __init__(self, nazwa: str = 'trapez', bok: float = 1, bok2: float = 1, bok3: float = 1, bok4: float = 1, wys: float = 1) -> None:
        super().__init__(nazwa)
        self.bok = bok
        self.bok2 = bok2
        self.bok3 = bok3
        self.bok4 = bok4
        self.wys = wys
        
    def poleFigury(self) -> float:
        return 1/2 * (self.bok * self.bok2) * self.wys
    
    def obwódFigury(self) -> float:
        return self.bok + self.bok2 + self.bok3 + self.bok4
    

    
class Deltoid(Prostokat):
    
    def __init__(self, nazwa: str = 'deltoid', bok: float = 1, bok2: float = 1, przek1: float = 1, przek2: float = 1) -> None:
        super().__init__(nazwa, bok, bok2)
        self.przek1 = przek1
        self.przek2 = przek2
        
    def poleFigury(self) -> float:
        return 1/2 * self.przek1 * self.przek2
    
    def obwódFigury(self) -> float:
        return super().obwódFigury()
    
class Rownoleglobok(Prostokat):
    
    def __init__(self, nazwa: str = 'równoległobok', bok: float = 1, bok2: float = 1, wys: float = 1) -> None:
        super().__init__(nazwa, bok, bok2)
        self.wys = wys
        
    def poleFigury(self) -> float:
        return self.bok * self.wys
    
    def obwódFigury(self) -> float:
        return super().obwódFigury()
    
    
class Trojkat(Figura):
    def __init__(self, nazwa: str = 'trójkąt', podstawa: float = 1, b: float = 1, c: float = 1, wys: float = 1) -> None:
        super().__init__(nazwa)
        self.podstawa = podstawa
        self.wys = wys
        self.b = b
        self.c = c
    
    def poleFigury(self):
        return 1/2 * self.podstawa * self.wys
    
    def obwódFigury(self):
        return self.podstawa + self.b + self.c
    
    
r = Rownoleglobok(bok=4, bok2=7, wys=14)
print("Obwód:", r.obwódFigury())
print("Pole:", r.poleFigury())