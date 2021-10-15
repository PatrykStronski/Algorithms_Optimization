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
    a = start[0]
    b = start[1]
    prev = (float('inf'), float('inf'))
    min = (float('inf'), float('inf'))
    min_val = float('inf')
    prev_val = 0.0
    func_calc = 0
    iter_calc = 0
    terminate = False

    while abs(prev_val - min_val) > precision:
        a1 = start[0] + GOLDEN_RATIO * (end[0] - start[0])
        a2 = end[0] - GOLDEN_RATIO * (end[0] - start[0])
        a_start = start[0]
        a_end = end[0]
        val1 = least_squares(approx, a1, b)
        val2 = least_squares(approx, a2, b)
        func_calc += 2
        while abs(a_start - a_end) > precision:
            iter_calc += 1
            if val1 <= val2:
                a_end = a2
                a2 = a1
                val2 = val1
                a1 = a_start + GOLDEN_RATIO * (a_end - a_start)
                val1 = least_squares(approx, a1, b)
            else:
                a_start = a1
                a1 = a2
                val1 = val2
                a2 = a_end - GOLDEN_RATIO * (a_end - a_start)
                val2 = least_squares(approx, a2, b)
            func_calc += 1

        if val1 < val2:
            prev = (min[0], min[1])
            min = (a1, b)
            prev_val = min_val
            min_val = val1
            a = a1
        else:
            prev = (min[0], min[1])
            min = (a2, b)
            prev_val = min_val
            min_val = val2
            a = a2

        b1 = start[1] + GOLDEN_RATIO * (end[1] - start[1])
        b2 = end[1] - GOLDEN_RATIO * (end[1] - start[1])
        b_start = start[1]
        b_end = end[1]
        val1 = least_squares(approx, a, b1)
        val2 = least_squares(approx, a, b2)
        func_calc += 2
        while abs(b_start - b_end) > precision:
            iter_calc += 1
            if val1 <= val2:
                b_end = b2
                b2 = b1
                val2 = val1
                b1 = b_start + GOLDEN_RATIO * (b_end - b_start)
                val1 = least_squares(approx, a, b1)
            else:
                b_start = b1
                b1 = b2
                val1 = val2
                b2 = b_end - GOLDEN_RATIO * (b_end - b_start)
                val2 = least_squares(approx, a, b2)
            func_calc += 1

        if val1 < val2:
            prev = (min[0], min[1])
            min = (a, b1)
            prev_val = min_val
            min_val = val1
            b = b1
        else:
            prev = (min[0], min[1])
            min = (a, b2)
            prev_val = min_val
            min_val = val2
            b = b2

        if abs(prev[0]-min[0]) > precision and abs(prev[1]-min[1]) > precision:
            return (min_val, min, func_calc, iter_calc)
        
    return (min_val, min, func_calc, iter_calc)

def neldar_mead(approx_: Callable, input: float, y: float, start: (float, float), end: (float, float), precision: float) -> ((float, float), int):
    pass