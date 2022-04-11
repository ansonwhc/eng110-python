import os
import math, datetime, sys

working_dir = os.getcwd()


def return_user_id():
    print(os.getuid())


def return_user_name():
    print(os.uname())


def operating_system_information():
    print(os.cpu_count())


def current_date():
    print(datetime.date.today())


def current_path():
    for path in sys.path:
        print(path)


def give_remainder():
    print(math.remainder(1, 5))


if __name__ == "__main__":
    current_path()
