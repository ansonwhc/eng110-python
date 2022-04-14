# take mass
# divide by 3
# round down
# subtract 2

# examples:
# 12 ==> 2
# 14 ==> 2
# 1969 ==> 654
# 100756 ==> 33583

# Pseudocode
# Function: fuel required from mass
# Input: Mass (int)
# (mass / 3) round down - 2
# Output: Fuel required (int)

# part 1
def get_fuel_requirement(mass: int) -> int:
    fuel = mass // 3 - 2
    return fuel

# part 2
def get_recur_fuel_requirement(mass: int) -> int:
    total_fuel = 0
    fuel = mass // 3 - 2
    if fuel > 0:
        total_fuel += fuel
        add_fuel = get_recur_fuel_requirement(fuel)
        total_fuel += add_fuel
    return total_fuel


if __name__ == "__main__":
    # part 1
    # total = 0
    # with open('input.txt', 'r') as input_file:
    #     for line in input_file.readlines():
    #         mass = int(line.strip())
    #         total += get_fuel_requirement(mass)
    # print(total)

    # part 2
    # print(get_recur_fuel_requirement(14))  # ==> 2
    # print(get_recur_fuel_requirement(100756))  # ==> 50346
    total = 0
    with open('input.txt', 'r') as input_file:
        for line in input_file.readlines():
            mass = int(line.strip())
            total += get_recur_fuel_requirement(mass)
    print(total)


