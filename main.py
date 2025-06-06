import math

# FizzBuzz Variant
def fizzBuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz") 
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz") 
        else:
            print(i) 

# fizzBuzz(15)


# Check for isPrime or not
def is_prime(n):
    if n <= 1:
        return False
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False
    return True

# print(is_prime(36))

