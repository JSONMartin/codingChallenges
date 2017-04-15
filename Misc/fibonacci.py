class Math(object):
    def fib_iterative(self, n):
        if n == 0 or n == 1: return n

        cur, last = 1, 0
        i = 2
        while i <= n:
            tmp = cur
            cur = last + cur
            last = tmp
            i += 1
        return cur

    def fib_recursive(self, n):
        if n == 0 or n == 1: return n

        return self.fib_recursive(n - 1) + self.fib_recursive(n - 2)

    def fib_dynamic(self, n):
        if n == 0 or n == 1: return n

        sequence = [0, 1]
        i = 2
        while (i <= n):
            sequence += [sequence[i-1] + sequence[i-2]]
            i += 1
        return sequence[-1]

testVal = 1

res = Math().fib_iterative(testVal)
print(res)
res = Math().fib_recursive(testVal)
print(res)
res = Math().fib_dynamic(testVal)
print(res)