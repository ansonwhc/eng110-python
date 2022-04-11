# Inheritance
from Animal import Animal


class Reptile(Animal):
    def __init__(self):
        super().__init__()

        self.cold_blooded = True
        self.tetrapad = None
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None

    def seek_head(self):
        print("It is too cold, I need heat!")

    def hunt(self):
        print("I am hunting my prey")

    def use_venom(self):
        print("I am using my venom")

    def attract_mate_through_scent(self):
        print("I am looking for a relationship")

if __name__ == "__main__":
    jeremy = Reptile()
    jeremy.seek_head()
    jeremy.eat()