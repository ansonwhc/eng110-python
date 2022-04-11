# Write a program that prints the numbers from 1 to 100. \
# But for multiples of 3 print “Fizz” instead of the number \
# and for the multiples of 5 print “Buzz”. \
# For numbers which are multiples of both 3 and 5 print “FizzBuzz”

def evaluate(num):
    add = ""
    if num % 3 == 0:
        add += "Fizz"
    if num % 5 == 0:
        add += "Buzz"
    to_return = add if add != "" else num

    return to_return


def if_fizzbuzz(user_input=None):
    if user_input is None:
        for i in range(1, 101):
            to_print = evaluate(num=i)
            print(to_print)
    else:
        assert isinstance(user_input, (int, float)),\
            f"Input type not recognized, input type: {type(user_input)}"
        user_input = int(user_input)
        to_print = evaluate(user_input)
        print(to_print)


if __name__ == "__main__":
    print("User test run:")
    if_fizzbuzz(15)
    print("From 1-100:")
    if_fizzbuzz()
