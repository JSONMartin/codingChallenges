from sympy import Symbol, symbols, factor, sympify, expand, pprint, init_printing, solve
from sympy.core.sympify import SympifyError

def tests():
    x, y, z = symbols('x,y,z')
    #print(x + x + 1)
    expr = x**2 - y**2
    factors = factor(expr)
    print(factors, " | ", expand(factors))
    pprint(expand(factors))

def printSeries(n, val):
    init_printing(order='rev-lex')
    x = Symbol('x')
    expr = x
    for i in range(2, n + 1):
        expr += (x**i / i)
    pprint(expr)

    res = expr.subs({x: val})
    print(res)

#printSeries(5, 1.2)

def calculateEquationFromStringInput():
    expr = input("Enter a math formula: ")
    while expr != "done":
        try:
            print(expr)
            expr = sympify(expr)
            print(expr)
        except:
            print("invalid formula")

        expr = input("Enter a math formula: ")

#calculateEquationFromStringInput()

def product(expr1, expr2):
    prod = expand(expr1 * expr2)
    print(prod)

expr1 = sympify("x ** 2 + x * 2 + x")
expr2 = sympify("x ** 3 + x * 3 + x")
product(expr1, expr2)

def solveEquation():
    x, a, b, c = Symbol('x'), Symbol('a'), Symbol('b'), Symbol('c')
    
    #expr = x ** 2 + 5 * x + 4
    #expr = x ** 2 + x + 1
    expr = a*x*x + b*x + c
    print(solve(expr, x, dict=True))

solveEquation()