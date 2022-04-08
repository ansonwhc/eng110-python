# str methods

def f_str_print():
    number = 10
    fruit = "apples"
    to_print = f"There are {number} {fruit}."
    print(to_print)


def age_input():
    age = input("Age: \n")
    while not age.isnumeric():
        print("Input type not accepted.\nPlease try again.\n")
        age = age_input()
    return age


def user_input():
    name = input("Name: \n").capitalize()
    age = age_input()

    class_input = input(f"Which class (e.g. 'str', 'float', 'int', 'complex') would you like to learn about:\n").strip()

    to_print_1 = f"Hello {name} ({age} years old)."
    to_print_2 = f"Class {class_input} includes methods: \n{dir(eval(class_input))}"

    print(f"{to_print_1}\n{to_print_2}")


if __name__=="__main__":
    # f_str_print()
    user_input()
