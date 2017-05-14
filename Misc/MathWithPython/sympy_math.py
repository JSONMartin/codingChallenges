from sympy import Symbol, symbols, factor, sympify, expand, pprint, init_printing

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

def calculateEquationFromStringInput():
    expr = input("Enter a math formula: ")
    print(expr)
    expr = sympify(expr)
    print(expr)


printSeries(5, 1.2)
calculateEquationFromStringInput()




