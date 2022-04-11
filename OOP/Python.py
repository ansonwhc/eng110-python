from Snake import Snake


class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(selfself):
        print("Ok, hand me the stretchy pants")

    def constrict(self):
        print("and...squeeeeeze")

    def climb(self):
        print("Up we go")

    def shed_skin(self):
        print("I am growing out of this now")


if __name__ == "__main__":
    peter = Python()
    peter.shed_skin()
