class Dog:
    def __init__(self, age, name, colour):
        self.animal_kind = "canine"
        self.name = name
        self.colour = colour

    def __str__(self):
        return f"A {self.age} years old dog"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A {self.age * 7} dog-years old dog"
        else:
            return self.__str__()

    def bark(self):
        return "woof"


if __name__ == "__main__":
    fido = Dog(age=3,
               name="Lucky",
               colour="Brown")

    print(f"{fido:dog}")

