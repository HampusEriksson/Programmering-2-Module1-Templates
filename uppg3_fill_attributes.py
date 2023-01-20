# Ditt namn
# Din klass
# Datum

# Alternativ 1
# Skriv färdigt init-metoden så att alla metoder fungerar

class Bottle:
    def __init__(self) -> None:
        # TODO Skriv metoden
        pass

    def __str__(self) -> str:
        return f"The bottle has {self.contents} ml left of the starting volume of {self.volume} ml.txt"

    def fill(self, ml):
        self.contents += ml
        if self.contents > self.volume:
            print("Water is spilling over, but the bottle is full.")
            self.contents = self.volume
        else:
            print(f"The bottle is now {100*self.contents/self.volume} % full.")

# Alternativ 2
# Skapa attribut till data-classen nedan
from dataclasses import dataclass

@dataclass
class Bottle:
    

    def __str__(self) -> str:
        return f"The bottle has {self.contents} ml left of the starting volume of {self.volume} ml.txt"

    def fill(self, ml):
        self.contents += ml
        if self.contents > self.volume:
            print("Water is spilling over, but the bottle is full.")
            self.contents = self.volume
        else:
            print(f"The bottle is now {100*self.contents/self.volume} % full.")