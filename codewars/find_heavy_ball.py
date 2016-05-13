#Source: http://www.codewars.com/kata/544034f426bc6adda200000e/

'''
There are 8 balls numbered from 0 to 7. Seven of them have the same weight. One is heavier. Your task is to find it's number.

Your function findBall will receive single argument - scales object. The scales object contains an internally stored array of 8 elements (indexes 0-7), each having the same value except one, which is greater. It also has a public method named getWeight(left, right) which takes two arrays of indexes and returns -1, 0, or 1 based on the accumulation of the values found at the indexes passed are heavier, equal, or lighter.

getWeight returns:

-1 if left pan is heavier

1 if right pan is heavier

0 if both pans weigh the same

Examples of scales.getWeight() usage:

scales.getWeight([3], [7]) returns -1 if ball 3 is heavier than ball 7, 1 if ball 7 is heavier, or 0 i these balls have the same weight.

scales.getWeight([3, 4], [5, 2]) returns -1 if weight of balls 3 and 4 is heavier than weight of balls 5 and 2 etc.

So where's the catch, you may ask. Well - the scales is very old. You can use it only TWICE before the scale breaks.

Note - Use scales.get_weight() in Python version.
'''

def find_ball(scales):
  w = scales.get_weight([0, 1, 2], [3, 4, 5])
  if w == 0: # They weigh the same, heavy ball is 6 or 7
      w2 = scales.get_weight([6], [7]) # Weigh and compare the 2 remaining balls
      if w2 == -1: return 6
      else: return 7
  elif w == -1: # Left group is heavier
      w2 = scales.get_weight([0], [1]) # Reweigh 2 of the 3 balls
      if w2 == -1: return 0
      elif w2 == 1: return 1
      else: return 2
  elif w == 1: # Right group is heavier
      w2 = scales.get_weight([3], [4]) # Reweigh 2 of the 3 balls
      if w2 == -1: return 3
      elif w2 == 1: return 4
      else: return 5