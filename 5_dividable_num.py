#  2520 is the smallest number that can be divided by each of the numbers from 1 to 10  without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#greatest common divisor
def gcd(a,b):
    while b != 0:
        a,b = b, a % b
    return a

# lowest common multiple
def lcm(a,b):
    return (a*b) // gcd(a,b)

def lowest_common_multiple():
    result = 1
    for i in range(1,21):
        result = lcm(result, i)
    return result

print(lowest_common_multiple())





