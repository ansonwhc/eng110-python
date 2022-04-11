def f():
    user_prompt = True
    while user_prompt:
        age = input("What is your age? ")
        if age.isdigit():
            age = int(age)
            if age < 18:
                to_print = "You are too young!"
                user_prompt = False
            elif age > 117:
                to_print = "Please be reasonable!"
            else:
                to_print = "Age accepted!"
                user_prompt = False
        else:
            to_print = f"Input type not recognized."
        print(to_print)


if __name__ == "__main__":
    f()
