# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, 
# the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

sum = 0



def fibonacci(n):
    fs = [1, 2]
    while fs[-1] < n:
        # generate the next term by adding the previous two terms
        next_term = fs[-1] + fs[-2]
        fs.append(next_term)
    return fs

a = fibonacci(4000000)

sum_of_even = 0
for b in a:
    if b%2 == 0:
        sum_of_even = sum_of_even + b
    else:
        pass
    
print(sum_of_even)

