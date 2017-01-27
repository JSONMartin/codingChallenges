# https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python
"""
A child plays with a ball on the nth floor of a big building the height of which is known

(float parameter "h" in meters, h > 0) .

He lets out the ball. The ball rebounds for example to two-thirds

(float parameter "bounce", 0 < bounce < 1)

of its height.

His mother looks out of a window that is 1.5 meters from the ground

(float parameters window < h).

How many times will the mother see the ball either falling or bouncing in front of the window

(return a positive integer unless conditions are not fulfilled in which case return -1) ?

Note

You will admit that the ball can only be seen if the height of the rebouncing ball is stricty greater than the window parameter.

Example:

h = 3, bounce = 0.66, window = 1.5, result is 3

h = 3, bounce = 1, window = 1.5, result is -1
"""
def bouncingBall(h, bounce, window, down = True, times_seen = 0):
    if not (0 < bounce < 1): return -1

    if h > window:
        if down:
            return bouncingBall(h, bounce, window, not down, times_seen + 1)
        else:
            return bouncingBall((h * bounce), bounce, window, not down, times_seen + 1)

    return times_seen -  1 if times_seen - 1 > 0 else -1

### TESTS
res = bouncingBall(3, .66, 1.5) #=> 3
#res = bouncingBall(3, 1, 1.5) #=> 3
#res = bouncingBall(30, 0.66, 1.5) #=> 15

print(res)