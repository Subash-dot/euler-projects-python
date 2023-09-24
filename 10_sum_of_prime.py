# The sum of the primes below  10  is  2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def is_prime(n):
    if n<=1:
        return False
    elif n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
    

sum_of_prime = 2
for j in range(2, 2000001):
    if is_prime(j):
        sum_of_prime += j
        
print(sum_of_prime)