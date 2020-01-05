#!/usr/bin/env python

import fileinput

def fuel_equation(mass):
    """Fuel required to launch a given module is based on its mass. 
    Specifically, to find the fuel required for a module, take its mass, 
    divide by three, round down, and subtract 2."""
    
    return mass // 3  - 2

def sum_fuel(inp):
    """The Fuel Counter-Upper needs to know the total fuel requirement. 
    To find it, individually calculate the fuel needed for the mass of 
    each module (your puzzle input), then add together all the fuel 
    values."""

    return sum(fuel_equation(int(line)) for line in inp)

if __name__ == '__main__':
    print(sum_fuel(fileinput.input()))