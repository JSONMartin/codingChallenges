## Easier to understand solution

def anagrams(word, words): ## Time Complexity (n log n + m log m) (due to sorting)
    word_sorted = sorted(word)
    return [w for w in words if sorted(w) == word_sorted]


## More time efficient solution

# def anagrams(orig_word, words):
#     orig_word_count = {}
#     results = []
#
#     for ch in orig_word: # Populate orig word count dict ## Time Complexity : O(n)
#         orig_word_count[ch] = orig_word_count.get(ch, 0) + 1
#
#     for word in words: ## Time Complexity : O(m)
#         is_anagram = True
#         word_count = orig_word_count.copy()
#
#         # Count Chars in current word
#         for ch in word:
#             count = word_count.get(ch, 0)
#             if count < 0: break
#             else: word_count[ch] = word_count.get(ch, 0) - 1
#
#         # Count chars remaining (if 0 for all letters, push into result)
#         for ch in word_count:
#             if word_count.get(ch, 0) != 0: is_anagram = False
#
#         if is_anagram: results.append(word)
#
#     #print("Results:"); print(results)
#     return results


##############
"""
TESTS
"""
##############
#result = anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
#result = anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) # => ['carer', 'racer']
result = anagrams('laser', ['lazing', 'lazy',  'lacer']) ## => []

print(result)