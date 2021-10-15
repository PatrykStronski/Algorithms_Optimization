import math
from typing import Callable

GOLDEN_RATIO = (3 - math.sqrt(5)) * 0.5

def exhaustive_search(func: Callable, start: float, end: float, precision: float) -> (float, int, int):
    division_number = int((end - start)/precision)
    min = start
    x = start
    min_val = func(start)
    func_calc = 1
    iters_calc = 0
    for ind in range(1, division_number):
        iters_calc += 1
        x += ind * precision
        val = func(x)
        func_calc += 1
        if min_val > val:
            min_val = val
            min = x
    return (min, func_calc, iters_calc)

def dichotomy(func: Callable, start: float, end: float, precision: float) -> (float, int, int):
    delta = precision * 0.5
    function_calcs = 0
    iters_calc = 0
    while abs(start - end) >= precision:
        iters_calc += 1
        x1 = (start + end - delta) * 0.5
        x2 = (start + end + delta) * 0.5
        y1 = func(x1)
        y2 = func(x2)
        if y1 <= y2:
            end = x2
        else:
            start = x1
        function_calcs += 2
    if y1 < y2:
        return (x1, function_calcs)
    return (x2, function_calcs, iters_calc)


def golden_selection(func: Callable, start: float, end: float, precision: float) -> (float, int, int):
    x1 = start + GOLDEN_RATIO * (end - start)
    x2 = end - GOLDEN_RATIO * (end - start)
    y1 = func(x1)
    y2 = func(x2)
    function_calcs = 2
    iters_calc = 0
    while abs(start - end) > precision:
        iters_calc += 1
        if y1 <= y2:
            end = x2
            x2 = x1
            y2 = y1
            x1 = start + GOLDEN_RATIO * (end - start)
            y1 = func(x1)
        else:
            start = x1
            x1 = x2
            y1 = y2
            x2 = end - GOLDEN_RATIO * (end - start)
            y2 = func(x2)
        function_calcs += 1
    
    if y1 < y2:
        return (x1, function_calcs, iters_calc)
    return (x2, function_calcs, iters_calc)
