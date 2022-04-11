# Create an input for money, type in a number,
# and make sure the format function transforms it into a money format e.g. 10.22

import anson_custom_test as a

input_array = [1., 5, 10.1234]


class Money:
    def __init__(self, money):
        self.money = money

    def __format__(self, format_spec):
        return format(format_spec, ".2f")


if __name__ == "__main__":
    for amount in input_array:
        M = Money(amount)
        print(M.__format__(amount))
