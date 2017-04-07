def palindrome(num,s):
    try:
        if num <= 0 or s < 0: raise Exception
        results = []

        while len(results) < s:
            if num >= 10 and str(num) == str(num)[::-1]: results.append(num)
            num += 1

        return results
    except:
        return "Not valid"