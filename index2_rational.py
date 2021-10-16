import matplotlib.pyplot as plt

from algorithms_2d import exhaustive_search, gauss_search, nelder_mead
from formulas import linear_approximation, rational_approximation, NOISY_DATA, X_ES

PRECISION = 0.001
START = (0.0, 0.0)
END = (1.0, 1.0)

print('Rational approximant')
plt.scatter(X_ES, NOISY_DATA, label='Y noisy data')

answ = exhaustive_search(rational_approximation, START, END, PRECISION)
print(f"Exhaustive Search: result={answ[0]} a={answ[1][0]}; b={answ[1][1]};function_calculation={answ[2]}; iterations={answ[3]}")

plt.plot(X_ES, [rational_approximation(x, answ[1][0], answ[1][1]) for x in X_ES], label='exhaustive search')

answ = gauss_search(rational_approximation, START, END, PRECISION)
print(f"Gauss Search: result={answ[0]} a={answ[1][0]}; b={answ[1][1]};function_calculation={answ[2]}; iterations={answ[3]}")

plt.plot(X_ES, [rational_approximation(x, answ[1][0], answ[1][1]) for x in X_ES], label='Gauss coordinate descent')

answ = nelder_mead(rational_approximation, START, END, PRECISION)
print(f"Nelder-Mead Search: result={answ[0]} a={answ[1][0]}; b={answ[1][1]};function_calculation={answ[2]}; iterations={answ[3]}")

plt.plot(X_ES, [rational_approximation(x, answ[1][0], answ[1][1]) for x in X_ES], label='Nelder-Mead method')

plt.xlabel('K-value')
plt.ylabel('Y-value')
plt.legend()
plt.grid(True)
plt.title('Data and its rational approximation')
plt.show()