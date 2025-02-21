from sympy import symbols, solve

x, y = symbols("x,y")
print(solve([
    x + y - 9, 
    5 * x + 4 * y - 1, 
    3 * x + 6 * y - 5
]))








