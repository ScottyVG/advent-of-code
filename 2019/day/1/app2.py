#!/usr/bin/env python

import fileinput

def fuel_equation(mass):
    """Fuel required to launch a given module is based on its mass. 
    Specifically, to find the fuel required for a module, take its mass, 
    divide by three, round down, and subtract 2."""
    return mass // 3  - 2

def get_total_fuel(mass):
    """So, for each module mass, calculate its fuel and add it to the 
    total. Then, treat the fuel amount you just calculated as the input 
    mass and repeat the process, continuing until a fuel requirement 
    is zero or negative."""

    total_fuel = 0

    while True:
        additional_fuel = fuel_equation(mass)
        if additional_fuel <= 0:
            break
        total_fuel += additional_fuel
        mass = additional_fuel

    return total_fuel

def sum_fuel(input):
    """then add together all the fuel values."""
    return sum(get_total_fuel(int(line)) for line in input)

if __name__ == '__main__':
    print(sum_fuel(fileinput.input()))
























# def get_fuel(mass):
#     return mass // 3  - 2


# def get_total_fuel(mass):
#     """Fuel for mass + fuel for fuel + fuel for fuel for fuel, etc."""
#     total_fuel = 0

#     while True:
#         additional_fuel = get_fuel(mass)
#         if additional_fuel <= 0:
#             break
#         total_fuel += additional_fuel
#         mass = additional_fuel

#     return total_fuel


# def sum_fuel(inp):
#     return sum(get_total_fuel(int(line)) for line in inp)