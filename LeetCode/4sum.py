class Solution(object):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
    """
    def fourSum(self, nums, target):
        pairs = {}
        length = len(nums)
        results = []
        results_dict = {}

        # Create all pair combinations, and store in pairs dict
        for i in range(length):
            for j in range(length - 1, i + 1, -1):
                if not (nums[i] + nums[j]) in pairs: pairs[nums[i] + nums[j]] = []
                pairs[nums[i] + nums[j]].append( {'nums_added': (nums[i], nums[j]), 'indexes': (i, j)} )

        # Check all pairs against combinations of other two numbers
        for i in range(length):
            for j in range(i+1, length):
                cur_total = nums[i] + nums[j]
                if (target - cur_total) in pairs: # Match found where is equal to target

                    # Ensure all 4 unique numbers, test i and j against indexes in pairs dict
                    for idx in pairs[target - cur_total]:
                        index = idx['indexes']

                        if i in index or j in index: continue
                        else:
                            result = sorted([nums[i], nums[j], idx['nums_added'][0], idx['nums_added'][1]])
                            if str(result) in results_dict: # Result already in dictionary, increase count
                                results_dict[str(result)] += 1
                            else: # Result not already in dict, add to results array
                                results_dict[str(result)] = 1
                                results.append(result)
        return results

s = Solution()
"""
TESTS
"""

#res = s.fourSum([1, 0, -1, 0, -2, 2], 0)
res = s.fourSum([-497,-494,-484,-477,-453,-453,-444,-442,-428,-420,-401,-393,-392,-381,-357,-357,-327,-323,-306,-285,-284,-263,-262,-254,-243,-234,-208,-170,-166,-162,-158,-136,-133,-130,-119,-114,-101,-100,-86,-66,-65,-6,1,3,4,11,69,77,78,107,108,108,121,123,136,137,151,153,155,166,170,175,179,211,230,251,255,266,288,306,308,310,314,321,322,331,333,334,347,349,356,357,360,361,361,367,375,378,387,387,408,414,421,435,439,440,441,470,492], 1682)
print(res)
"""
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
