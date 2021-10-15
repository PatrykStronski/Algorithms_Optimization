from formulas import x_pow3, x_sin_rational, x_abs
from algorithms import exhaustive_search, dichotomy, golden_selection

PRECISION = 0.001

print('x3 - results')
dt = exhaustive_search(x_pow3, 0.0, 1.0, PRECISION)
print(dt)
dt = dichotomy(x_pow3, 0.0, 1.0, PRECISION)
print(dt)
dt = golden_selection(x_pow3, 0.0, 1.0, PRECISION)
print(dt)

print('|x-0.2| - results')
dt = exhaustive_search(x_abs, 0.0, 1.0, PRECISION)
print(dt)
dt = dichotomy(x_abs, 0.0, 1.0, PRECISION)
print(dt)
dt = golden_selection(x_abs, 0.0, 1.0, PRECISION)
print(dt)

print('x*sin(1/x) - results')
dt = exhaustive_search(x_sin_rational, 0.01, 1.0, PRECISION)
print(dt)
dt = dichotomy(x_sin_rational, 0.01, 1.0, PRECISION)
print(dt)
dt = golden_selection(x_sin_rational, 0.01, 1.0, PRECISION)
print(dt)