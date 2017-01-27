# https://www.codewars.com/kata/5709aa85fe2d012f1d00169c/train/python

"""
Instructions
Output
The professional Russian, Dmitri, from the popular youtube channel FPSRussia has hired you to help him move his arms cache between locations without detection by the authorities. Your job is to write a Shortest Path First (SPF) algorithm that will provide a route with the shortest possible travel time between waypoints, which will minimize the chances of detection. One exception is that you can't travel through the same waypoint twice. Once you've been seen there is a higher chance of detection if you travel through that waypoint a second time.

Your function shortestPath will take three inputs, a topology/map of the environment, along with a starting point, and an ending point. The topology will be a dictionary with the keys being the different waypoints. The values of each entry will be another dictionary with the keys being the adjacent waypoints, and the values being the time it takes to travel to that waypoint.

Take the following topology as an example:

 topology = {'a' : {'b': 10, 'c': 20},
             'b' : {'a': 10, 'c': 20},
             'c' : {'a': 10, 'b': 20} }
In this example, waypoint 'a' has two adjacent waypoints, 'b' and 'c'. And the time it takes to travel from 'a' to 'b' is 10 minutes, and from 'a' to 'c' is 20 minutes. It's important to note that the time between these waypoints is one way travel time and can be different in opposite directions. This is highlighted in the example above where a->c takes 20 minutes, but c->a takes 10 minutes.

The starting and ending points will passed to your function as single character strings such as 'a' or 'b', which will match a key in your topology.

The return value should be in the form of a list of waypoints that make up the shortest travel time. If there multiple paths that have equal travel time, then you should choose the path with the least number of waypoints. If there are still multiple paths with equal travel time and number of waypoints, then you should return a list of lists with the multiple options.

Here are a few examples:

#Topology
#      b--d--g
#     /   |   \
#    /    |    \
#   a-----e-----h
#    \     \   /
#     \     \ /
#      c-----f
topology = {'a' : {'b': 10, 'c': 20, 'e':20},
            'b' : {'a': 10, 'd': 20},
            'c' : {'a': 10, 'f': 20},
            'd' : {'b': 10, 'e': 20, 'g': 20},
            'e' : {'a': 10, 'd': 20, 'f': 20},
            'f' : {'c': 10, 'e': 20, 'h': 20},
            'g' : {'d': 10, 'h': 20},
            'h' : {'g': 10, 'f': 20},
}

Two solutions with a time of 40:
shortestPath(topology, 'a', 'f') == [['a', 'c', 'f'],['a', 'e', 'f']]

One solution with a time of 20:
shortestPath(topology, 'a', 'e') == ['a', 'e']
"""

def shortestPath(topology, startPoint, endPoint, distance = 0, visited = None, results = None):
    # Required because Python default variables are buggy
    if visited == None:
        visited = []
    if results == None:
        results = []

    if len(visited) == 0: visited.append(startPoint)

    if startPoint == endPoint:
        results.append((distance, visited))
        return results

    for point in topology[startPoint]:
        point_distance = topology[startPoint][point]

        if point not in visited:
            shortestPath(topology, point, endPoint, distance + point_distance, visited[:] + [point], results)

    if len(results) > 0:
        shortest_distance = min(results)[0]
        shortest_length = len(min(results, key = lambda x: len(x[1]) if x[0] == shortest_distance else float('inf'))[1])
        shortest_paths = [p[1] for p in results if (p[0] == shortest_distance) and (len(p[1]) == shortest_length)]
        return shortest_paths[0] if len(shortest_paths) == 1 else shortest_paths
    else:
        return results

### TESTS

topology = {'a' : {'b': 10, 'c': 20, 'e':20},
            'b' : {'a': 10, 'd': 20},
            'c' : {'a': 10, 'f': 20},
            'd' : {'b': 10, 'e': 20, 'g': 20},
            'e' : {'a': 10, 'd': 20, 'f': 20},
            'f' : {'c': 10, 'e': 20, 'h': 20},
            'g' : {'d': 10, 'h': 20},
            'h' : {'g': 10, 'f': 20},
            }

#Two solutions with a time of 40:
# res = shortestPath(topology, 'a', 'c') #== [['a', 'c', 'f'],['a', 'e', 'f']]
# print(res)
# print("-------------")
# print("-------------")
# print("-------------")
#
# res = shortestPath(topology, 'a', 'e') #== [['a', 'c', 'f'],['a', 'e', 'f']]
# print(res)
topology = {'a': {'c': 20, 'b': 10, 'd': 20}, 'c': {'a': 10, 'b': 20, 'e': 20}, 'b': {'a': 10, 'c': 20, 'e': 20, 'd': 20, 'g': 20, 'f': 20}, 'e': {'c': 20, 'b': 10, 'g': 20}, 'd': {'a': 10, 'b': 20, 'f': 20}, 'g': {'b': 10, 'e': 20, 'f': 20}, 'f': {'b': 10, 'd': 20, 'g': 20} }
print("-------------")
print("-------------")
print("-------------")
res = shortestPath(topology, 'c', 'g') #== [['a', 'c', 'f'],['a', 'e', 'f']]
print(res)
#print(results)