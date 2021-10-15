from typing import Callable
from formulas import least_squares
import math

GOLDEN_RATIO = (3 - math.sqrt(5)) * 0.5

def exhaustive_search(approx: Callable, start: (float, float), end: (float, float), precision: float) -> (float, (float, float), int, int):
    division_number_a = int((end[0] - start[0])/precision)
    division_number_b = int((end[1] - start[1])/precision)
    min = start
    a = start[0]
    b = start[1]
    min_val = float('inf')
    func_calc = 0
    iter_calc = 0
    for ind_a in range(0, division_number_a):
        a += ind_a * precision
        b = start[1]
        for ind_b in range(0, division_number_b):
            iter_calc += 1
            b += ind_b * precision
            val = least_squares(approx, a, b)
            func_calc += 1
            if min_val > val:
                min_val = val
                min = (a, b)
    return (min_val, min, func_calc, iter_calc)

def gauss_search(approx: Callable, start: (float, float), end: (float, float), precision: float) -> (float, (float, float), int, int):
    division_number_a = int((end[0] - start[0])/precision)
    division_number_b = int((end[1] - start[1])/precision)
    a = start[0]
    b = start[1]
    prev = (a,b)
    min = (float('inf'), float('inf'))
    min_val = float('inf')
    func_calc = 0
    iter_calc = 0
    terminate = False

    while abs(prev[0]-min[0]) > precision and abs(prev[1]-min[1]) > precision:
        print(prev)
        print(min)
        print(min_val)

        for ind_a in range(0, division_number_a):
            iter_calc += 1
            a += ind_a * precision
            val = least_squares(approx, a, b)
            func_calc += 1
            if min_val > val:
                if abs(min_val-val) < precision:
                    return (val, (a, b), func_calc, iter_calc)
                min_val = val
                prev = (min[0], prev[1])
                min = (a, b)

        a = min[0]
        b = start[1]
        
        for ind_b in range(0, division_number_b):
            iter_calc += 1
            b += ind_b * precision
            val = least_squares(approx, a, b)
            func_calc += 1
            if min_val > val:
                if abs(min_val-val) < precision:
                    return (val, (a, b), func_calc, iter_calc)
                min_val = val
                prev = (prev[0], min[1])
                min = (a, b)
        
        b = min[1]
        a = start[0]
        
    return (min_val, min, func_calc, iter_calc)

def neldar_mead(approx_: Callable, input: float, y: float, start: (float, float), end: (float, float), precision: float) -> ((float, float), int):
    pass