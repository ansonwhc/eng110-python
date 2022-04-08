# str methods

def f_str_print():
    number = 10
    fruit = "apples"
    to_print = f"There are {number} {fruit}."
    print(to_print)


def user_input():
    # ask a few question
    # collect text and numbers
    # respond with a mess that includes the input entries
    name = input("Name: \n")
    age = input("Age: \n")
    height = input("Height (cm): \n")

    to_print = f"{name} is {age} years young, and {height}cm tall."
    print(to_print)


if __name__=="__main__":
    # f_str_print()
    user_input()
