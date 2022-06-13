# Intcode program ==> list(ints)
# Intcode[0] == opcode == (1 | 2 | 99)

# opcode == 99 >>> halt

# opcode == 1 >>> addition from two positions and stores result in third position
#   read three ints right after opcode 1
#   two ints after 1 indicate the positions of the ints for the addition
#   the third position indicates the pos where the result is stored

# opcode == 2 >>> multiply

# after the op, move forward 4 positions

def f(intcode: list,
      idx: (int, None) = 0) -> list:
    if intcode[idx] == 1:
        result = sum([intcode[idx+1], intcode[idx+2]])
        intcode[idx+3] = result
        print('1', intcode)
        idx += 4
        intcode = f(intcode, idx)

    elif intcode[idx] == 2:
        print(intcode)
        result = intcode[idx+1] * intcode[idx+2]
        intcode[idx+3] = result
        print('2', intcode)
        idx += 4
        intcode = f(intcode, idx)

    elif intcode[idx] == 99:
        pass

    else:
        print("unrecognised")

    return intcode


if __name__ == "__main__":
    result = f([1, 0, 0, 0, 99])
    print(result)


