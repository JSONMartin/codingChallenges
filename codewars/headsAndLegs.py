"""
# https://www.codewars.com/kata/574c5075d27783851800169e/train/python
# Description

Everybody has probably heard of the animal heads and legs problem from the earlier years at school. It goes:

“A farm contains chickens and cows. There are x legs and y heads. How many chickens and cows are there?”

Where x <= 1000 and y <=1000

#Task

Assuming there are no other types of animals, work out how many of each animal are there.

Return a tuple in Python - (Heads, Legs) and an array list - [Heads, Legs]/{Heads, Legs} in all other languages

If either the heads & legs is negative, the result of your calculation is negative or the calculation is a float return "No solutions" (no valid cases).

In the form:

(Heads, Legs) = (72, 200)

VALID - (72, 200) =>             (44 , 28)
                             (Chickens, Cows)

INVALID - (72, 201) => "No solutions"
However, if 0 heads and 0 legs are given always return [0, 0] since zero heads must give zero animals.

There are many different ways to solve this, but they all give the same answer.

You will only be given integers types - however negative values (edge cases) will be given.

Happy coding!
"""
def animals(heads, legs):
    # x + y = heads
    # 4x + 2y = legs (x = chickens, y = cows)
    if legs % 2 != 0: return 'No solutions'

    y = int((legs - (4 * heads)) / -2)
    x = int(heads - y)
    print(y, x)

    return (y, x) if y >= 0 and x >= 0 else 'No solutions'

animals(72, 200)