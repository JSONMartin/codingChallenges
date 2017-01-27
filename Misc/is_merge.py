def is_merge(s, part1, part2):
    match_found = False
    def check_merge(w, w1, w2):
        nonlocal match_found
        if len(w) == 0 and len(w1) == 0 and len(w2) == 0:
            match_found = True
            return True
        if len(w1) > 0 and len(w) > 0 and w1[0] == w[0]: check_merge(w[1:], w1[1:], w2)
        if len(w2) > 0 and len(w) > 0 and w2[0] == w[0]: check_merge(w[1:], w1, w2[1:])

    check_merge(s, part1, part2)
    return match_found

print(is_merge('Bananas from Bahamas', 'Bahas', 'Bananas from am'))