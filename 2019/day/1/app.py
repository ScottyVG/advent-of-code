#!/usr/bin/env python

import fileinput

def fuel_equation(mass):
    """Fuel required to launch a given module is based on its mass. 
    Specifically, to find the fuel required for a module, take its mass, 
    divide by three, round down, and subtract 2."""
    return mass // 3  - 2

def get_total_fuel(mass):
    """The Fuel Counter-Upper needs to know the total fuel requirement. 
    To find it, individually calculate the fuel needed for the mass of 
    each module (your puzzle input), then add together all the fuel 
    values."""

    total_fuel = 0

    total_fuel = fuel_equation(mass)

    # while True:
    #     additional_fuel = fuel_equation(mass)
    #     if additional_fuel <= 0:
    #         break
    #     total_fuel += additional_fuel
    #     mass = additional_fuel

    return total_fuel

def sum_fuel(inp):
    """then add together all the fuel values."""
    return sum(get_total_fuel(int(line)) for line in inp)

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