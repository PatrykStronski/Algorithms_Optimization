import math
import numpy as np
from typing import Callable
from random import random

DELTA_NOISE =  np.random.randn(100)
alpha = random()
beta = random()

"""function from the task 1b"""
def x_pow3(x: float) -> float:
    return x ** 3

"""function from the task 1b"""
def x_abs(x: float) -> float:
    res = x - 0.2
    if res < 0:
        return res * -1
    return res

"""function from the task 1c"""
def x_sin_rational(x: float):
    return x * math.sin(1/x)

"""noise generator from 2nd task"""
def gen_noisy_data(alpha: float, beta: float, k: int) -> float:
    delta = DELTA_NOISE[k]
    return alpha * k / 100 + beta + delta

"""Linear approximant of the function from the first task"""
def linear_approximation(x: float, a: float, b: float) -> float:
    return x*a + b

"""Rational approximant of the function from the first task"""
def rational_approximation(x: float, a: float, b: float) -> float:
    return a / (1 + b * x)

NOISY_DATA = [] 
X_ES = []

for k in range(0,100):
    NOISY_DATA.append(gen_noisy_data(alpha, beta, k))
    X_ES.append(k/100)

"""Least squares method that for function func calculates lest square sum"""
def least_squares(func: Callable, a: float, b: float) -> float:
    sum = 0
    for k in range(0,100):
        y = NOISY_DATA[k]
        x = X_ES[k]
        sum += (func(x, a, b) - y) **2
    return sum