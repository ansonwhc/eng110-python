class Animal:
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("I am breathing")

    def eat(self):
        print("I am eating")

    def procreate(self):
        print("Time to find a mate")

    def move(self):
        print("I am moving")


if __name__ == "__main__":
    cat = Animal()
    cat.breathe()

