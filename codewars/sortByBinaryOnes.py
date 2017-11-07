def sort_by_binary_ones (num_list):
    def binConvert(n): return bin(n)[2:]
    def binSum(n): return [int(x) for x in binConvert(n)].count(1)
    sortFn = lambda num: (binSum(num), 0 - len(str(binConvert(num))), 0 - num)

    return sorted(num_list, key=sortFn, reverse=True)
