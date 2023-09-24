# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13
# What is the 10001st prime number?


def is_prime(n):
    if n%2 == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
        
prime = [2]
for i in range(2, 1000001):
    if is_prime(i):
        prime.append(i)
        

print(prime[10001-1])




