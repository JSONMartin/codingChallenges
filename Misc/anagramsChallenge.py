"""
Input: ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
Result: ['arm', 'ram', 'act', 'cat', 'bat', 'tab']
"""
from collections import OrderedDict

class Anagram(object):
    def group_anagrams(self, items):
        od = OrderedDict(); results = []
        
        for item in items:
            key = str(sorted(set(item)))
            od[key] = od.get(key, []) + [item]
        
        for key in od:
            results += sorted(od[key])
        #print(results)
        return results

res = Anagram().group_anagrams(['ram', 'act', 'arm', 'bat', 'cat', 'tab'])
print(res)