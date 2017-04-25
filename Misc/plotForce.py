'''
test
'''

import matplotlib.pyplot as plt
import math

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x coord')
    plt.ylabel('y coord')
    plt.title('Motion of ball')
    plt.show()

# def generate_F_r():
#     r = range(100, 1001, 50)
#     F = []
#     G = 6.674*(10**-11)
    
#     m1 = .5 # kg
#     m2 = 1.5 # kg

#     for distance in r:
#         F += [G*(m1*m2)/(distance**2)]
    
#     draw_graph(r, F)

# #generate_F_r()

# def frange(start, final, increment):
#     numbers = []
    
#     while start < final:
#         numbers += [start]
#         start += increment
    
#     return numbers

# # Theta is degree of throw projectile
# def draw_trajectory(u, theta):
#     theta = math.radians(theta)
#     sin = math.sin; cos = math.cos
#     g = 9.8

#     # Time of Flight
#     t_flight = 2 * u * sin(theta) / g
    
#     intervals = frange(0, t_flight, .001)
#     print(intervals)

#     x, y = [], []
#     for t in intervals:
#         x += [u*cos(theta)*t]
#         y += [u*sin(theta)*t - .5*g*t*t]
    
#     draw_graph(x, y)

# for i in [20, 40, 60]:
#     draw_trajectory(i,60)
# plt.legend([20, 40, 60])
# plt.show()

memo = {}
def fibo(n):
    if n in memo: return memo[n]
    if n == 0 or n == 1: return n
    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]

res = fibo(5)
print(res)

fibos = [fibo(i) for i in range(1,100)]

fiboRatio = []
for _ in range(1, len(fibos)):
    fiboRatio.append(fibos[_] / fibos[_ - 1])
print(fibos)
draw_graph(range(1, len(fibos)), fiboRatio)
print(fibos)
