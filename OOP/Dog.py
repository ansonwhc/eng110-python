class Dog:

    animal_kind = "canine1"

    def __init__(self):
        self.animal_kind = "canine"

    def bark(self):

        return "woof"


if __name__ == "__main__":
    lassie = Dog()
    fido = Dog()

    fido.animal_kind = "asdf"
    print(fido.animal_kind)
    print(lassie.animal_kind)
    pass
