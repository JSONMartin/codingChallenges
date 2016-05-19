#Source: http://www.codewars.com/kata/544aed4c4a30184e960010f4
def divisors(integer):
    divisor_list = []
    for x in range(2, int(integer / 2) + 1):
        if integer % x == 0: divisor_list.append(x)
    return divisor_list if divisor_list != [] else '%d is prime' % integer

def divisors_refactored(integer):
    result = [i for i in range(2, int(integer / 2) + 1) if integer % i == 0]
    return result if result else '%d is prime' % integer