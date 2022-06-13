def positional_func(*args):
    for arg in args:
        print(arg)


def greeting(name: str) -> str:
    message = f"Hello {name}"
    print(message)
    return message


def division(num: float = 1, denom: float = 1) -> float:
    return num / denom


def addition(*nums: float) -> float:
    return sum(nums)


def multiply(*nums: float) -> float:
    pass


if __name__ == "__main__":
    # print(positional_func(2, 2))
    # print(division(2, 3))
    print(addition(1, 2))