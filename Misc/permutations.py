"""
Test Cases
* None -> None
* '' -> ''
* 'AABC' -> ['AABC', 'AACB', 'ABAC', 'ABCA',
             'ACAB', 'ACBA', 'BAAC', 'BACA',
             'BCAA', 'CAAB', 'CABA', 'CBAA']
"""
from timeit import default_timer as timer
start = timer()


class Permutations(object):
    def find_permutations(self, string):
        if not string or string == None: return string
        permutations = set()

        def generatePermutation(current = '', remaining = []):
            #print(remaining)
            if len(remaining) == 0:
                permutations.add(current)
                return
            for idx, letter in enumerate(remaining):
                generatePermutation(current + letter, remaining[:idx] + remaining[idx + 1:])

        generatePermutation('', list(string))
        return list(sorted(permutations))

### Reference solution (34.86 seconds with 'ABCDEFGIJH' test string)
# from collections import OrderedDict
# class Permutations(object):
#     def _build_counts_map(self, string):
#         counts_map = OrderedDict()
#         for char in string:
#             if char in counts_map:
#                 counts_map[char] += 1
#             else:
#                 counts_map[char] = 1
#         return counts_map

#     def find_permutations(self, string):
#         if string is None or string == '':
#             return string
#         counts_map = self._build_counts_map(string)
#         curr_results = []
#         results = []
#         self._find_permutations(counts_map, curr_results, results, len(string))
#         return results

#     def _find_permutations(self, counts_map, curr_result, results, input_length):
#         for char in counts_map:
#             if counts_map[char] == 0:
#                 continue
#             curr_result.append(char)
#             counts_map[char] -= 1
#             if len(curr_result) == input_length:
#                 results.append(''.join(curr_result))
#             else:
#                 self._find_permutations(counts_map, curr_result,
#                                         results, input_length)
#             counts_map[char] += 1
#             curr_result.pop()

### TESTS
#Permutations().find_permutations('AABC')
res = Permutations().find_permutations('ABCDEFGIJH')

end = timer()
print("%f second(s)" % (end - start))

#print(res)
