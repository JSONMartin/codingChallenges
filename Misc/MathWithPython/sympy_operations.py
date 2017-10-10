from sympy import FiniteSet, pi
# Unions & Intersections
s = FiniteSet(1, 2, 3)
t = FiniteSet(2, 4, 6)

union = s.union(t)
print(union)

intersection = s.intersect(t)
print(intersection)

### Cartesian Products
cartesianProduct = s * t
print(cartesianProduct)

for elem in cartesianProduct:
    print(elem)

# Raise set to the power (calculate triplets)
cartesianProductCubed = s ** 3
for elem in cartesianProductCubed:
    print(elem)




def time_period(length, g):
    T = 2*pi*(length/g)**0.5
    return T

L = FiniteSet(15, 18, 21, 22.5, 25)
g_values = FiniteSet(9.8, 9.78, 9.83)
print('{0:^15}{1:^15}{2:^15}'.format('Length(cm)', 'Gravity(m/s^2)', 'Time period(s)'))
for elem in L*g_values:
    l = elem[0]
    g = elem[1]
    t = time_period(l/100, g)
    print('{0:^15}{1:^15}{2:^15}'.format(float(l), float(g), float(t)))