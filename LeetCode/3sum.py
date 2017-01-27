# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]
from collections import Counter

class Solution(object):
    def threeSum(self, nums):
        def add_unique_combo(combo, seen): # Helper method to only add unique combinations
            sorted_combo = sorted(combo)
            if not str(sorted_combo) in seen:
                results.append(sorted_combo)
                seen[str(sorted_combo)] = True

        length, results, seen, counter = len(nums), [], {}, Counter(nums)

        # Handle special cases
        if length < 3: return []
        elif 0 in counter and counter[0] >= 3: add_unique_combo([0, 0, 0], seen)

        # Iterate through counter dictionary looking for unique combos
        for i in counter:
            for j in counter:
                if i == j: continue # Current keys are the same, so skip

                target = -(i + j) # Set target to look for to equal 0 sum

                if (i == target or j == target):
                    if counter[target] > 1: add_unique_combo([i, j, target], seen)
                elif target in counter:
                    add_unique_combo([i, j, target], seen)

        return results

    def threeSumBeforeCleanup(self, nums):
        length, results, seen = len(nums), [], {}

        def addUnique(combo, seen):
            print("Combo from addUnique:" + str(combo))
            sortedCombo = sorted(combo)
            if not str(sortedCombo) in seen:
                results.append(sortedCombo)
                seen[str(sortedCombo)] = True

        if length < 3:
            return []

        counter = Counter(nums)

        for i in counter:
            for j in counter:
                if i == j: continue # Current keys are the same, so skip
                print("----")
                print("I:%d, J:%d" % (i, j))
                target = -(i + j)
                print("Target:%d" % target)
                # if (i == target or j == target):
                #     print("counter[target]:%d" % counter[target])
                #     if counter[target] > 1: addUnique([i, j, target], seen)
                #     #addUnique([i, j, target], seen)
                if (i == target or j == target):
                    if counter[target] > 1: addUnique([i, j, target], seen)
                elif target in counter:
                    addUnique([i, j, target], seen)
        return results






    # Three Sum, using hash map without sort
    # From: https://discuss.leetcode.com/topic/16990/python-hashmap-o-n-2
    def threeSumHashMapNoSort(self, nums):
        len_n = len(nums)
        numsDict = {} # count the appearance of each numbers
        res = []
        resSet = set([]) # a result set, use tuple
        if len_n < 3:
            return []
        for i in range(len_n):
            if nums[i] in numsDict:
                numsDict[nums[i]] += 1
            else:
                numsDict[nums[i]] = 1
        if 0 in numsDict: # handle the special 0 case
            if numsDict[0] >= 3:
                res.append([0,0,0])
                resSet.add((0,0,0))

        for i in numsDict:
            for j in numsDict:
                if i!=j:
                    i_j = -(i+j)
                    if i_j == j or i_j == i:
                        if numsDict[i_j]>1:
                            sortij = [i,j,-(i+j)]
                            sortij.sort()
                            if not tuple(sortij) in resSet:
                                resSet.add(tuple(sortij))
                                res.append(sortij)
                    elif i_j in numsDict:
                        sortij = [i,j,-(i+j)]
                        sortij.sort()
                        if not tuple(sortij) in resSet:
                            resSet.add(tuple(sortij))
                            res.append(sortij)
        return res


    # Three sum, implementing two sum function
    def twoSum(self, target, nums):
        n = len(nums)
        ret, d = [], {}
        for i in range(n):
            if nums[i] in d:
                ret.append([d[nums[i]], nums[i]])
            else:
                d[target - nums[i]] = nums[i]
        return ret

    def threeSumImplementTwoSum(self, num):
        if len(num) < 3:
            return []
        num.sort()
        n, res = len(num), []
        for i in range(n):
            if num[i] > 0:
                break
            for two in self.twoSum(-num[i], num[i+1:]):
                if [num[i]] + two not in res:
                    res.append([num[i]] + two)
        return res

    def threeSumImproved(self, arr, n = 0):
        results = []
        limits = 0, len(arr) - 1
        arr = sorted(arr)
        for i, target in enumerate(arr):
            lower, upper = limits
            while lower < i < upper:
                values = (arr[lower], target, arr[upper])
                tmp = sum(values)
                if not tmp:
                    results.append(values)
                lower += tmp <= 0
                upper -= tmp >= 0

        return results

    def threeSumWithHashTable(self, nums, n = 0): # Hash Map solution without sort (gets TLE)
        results, counter = {}, {}

        # Convert the array to a hash table, with indicies
        for i in range(len(nums)):
            n = nums[i]
            if n in counter: counter[n][i] = True
            else:
                counter[n] = {}
                counter[n][i] = True

        # Iterate through the array, checking if the third value equals zero
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                a, b = nums[i], nums[j]
                val_to_look_for = -(a + b)

                if val_to_look_for in counter:
                    indices = counter[val_to_look_for]

                    if len(indices) >= 3 or (not i in indices and not j in indices):
                        answer = sorted([nums[i], nums[j], val_to_look_for])
                        results[str(answer)] = answer

        return list(results.values())

    def threeSumSortedSolution(self, nums, n = 0): # Accepted solution on LeetCode
        results = []
        results_dict = {}
        nums.sort()

        for i in range(len(nums) - 2):
            a = nums[i]
            start = i + 1
            end = len(nums) - 1

            while start < end:
                b, c = nums[start], nums[end]
                total = a + b + c

                if total == n:
                    combo = sorted([a, b, c])
                    combo_key = str(combo)
                    if not combo_key in results_dict:
                        results_dict[combo_key] = True
                        results.append(combo)
                    end -= 1

                elif total > n:
                    end -= 1
                else:
                    start += 1

        return results

    def threeSumFromInterview(self, nums, n = 0): # Answer from Interview, O(n^3) [worst case]
        i, j, k = 0, 1, 2
        results = []
        results_dict = {}

        while i <= len(nums) - 3:
            total = nums[i] + nums[j] + nums[k]
            if total == n:
                combo = sorted([nums[i], nums[j], nums[k]])
                combo_key = str(combo)
                #print(str(combo_key))
                if not combo_key in results_dict:
                    results_dict[combo_key] = True
                    results.append(combo)

            if j == len(nums) - 2:
                i += 1
                j = i + 1
                k = j + 1
            elif k == len(nums) - 1:
                j += 1
                k = j + 1
            else:
                k += 1

        return results





### TESTING
#testArr = [-1,0,1,2,-1,-4]
testArr = [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6,7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6,7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6,7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6,7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6,7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6,7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6,7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6,7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6,7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6,7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6,7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6,7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6,7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6,7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6,7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
s = Solution()

res = s.threeSum(testArr)
#res = s.threeSumWithHashTable(testArr)
#res = s.threeSumSortedSolution(testArr)
#res = s.threeSumFromInterview(testArr)

#print(res)