from algorithms_2d import exhaustive_search, gauss_search, nelder_mead
from formulas import linear_approximation, rational_approximation

PRECISION = 0.001
START = (0.0, 0.0)
END = (1.0, 1.0)

print('Linear approximant')
#answ = exhaustive_search(linear_approximation, START, END, PRECISION)
#print(f"Exhaustive Search: result={answ[0]} a={answ[1][0]}; b={answ[1][1]};function_calculation={answ[2]}; iterations={answ[3]}")
answ = gauss_search(linear_approximation, START, END, PRECISION)
print(f"Gauss Search: result={answ[0]} a={answ[1][0]}; b={answ[1][1]};function_calculation={answ[2]}; iterations={answ[3]}")
answ = nelder_mead(linear_approximation, START, END, PRECISION)
print(f"Nelder-Mead Search: result={answ[0]} a={answ[1][0]}; b={answ[1][1]};function_calculation={answ[2]}; iterations={answ[3]}")

print('Rational approximant')
#answ = exhaustive_search(rational_approximation, START, END, PRECISION)
#print(f"Exhaustive Search: result={answ[0]} a={answ[1][0]}; b={answ[1][1]};function_calculation={answ[2]}; iterations={answ[3]}")
answ = gauss_search(rational_approximation, START, END, PRECISION)
print(f"Gauss Search: result={answ[0]} a={answ[1][0]}; b={answ[1][1]};function_calculation={answ[2]}; iterations={answ[3]}")
answ = nelder_mead(rational_approximation, START, END, PRECISION)
print(f"Nelder-Mead Search: result={answ[0]} a={answ[1][0]}; b={answ[1][1]};function_calculation={answ[2]}; iterations={answ[3]}")