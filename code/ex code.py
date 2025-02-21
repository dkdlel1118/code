from sympy import symbols, Eq, solve

# 변수 정의
x, y = symbols('x y')

# 연립방정식 정의
eq1 = Eq(x - y, -3)
eq2 = Eq(2*x + 5*y, 8)

# 연립방정식 풀기
solution = solve((eq1, eq2), (x, y))

print(solution)















