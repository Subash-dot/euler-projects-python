# <p>A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which,
# $$a^2 + b^2 = c^2.$$</p>
# <p>For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.</p>
# <p>There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>Find the product $abc$.</p>


# first_number = 0
# second_number = 0
# third_number = 0

# for i in range(2,500):
#     a = i
#     first_number = i

#     if first_number%2 != 0:
#         second_number = ((a*a)/2) - 0.5
#         third_number = ((a*a)/2) +0.5
#     else:
#         second_number = (a/2)*(a/2) - 1
#         third_number = (a/2)*(a/2) + 1


#     if 900<(first_number + second_number + third_number)<1100:
#         print(f"{first_number} + {second_number} + {third_number} = {first_number + second_number + third_number}")


for a in range(1, 1000):
    for b in range(1, 1000-a):
        c = 1000-b-a
        if a*a + b*b == c*c:
            print(f'{a}+{b}+{c}={a+b+c}')
            print(f'{(a*a)+(b*b)}={c*c}')
            print(a*b*c)


