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
    square_root = int(math.sqrt(n))
    for i in range(2, square_root + 1):
        if n % i == 0:
            return False
    return True


# print(is_prime(36))

# Palindrome Checker


def palindromeChecker(string):
    x = 0
    y = len(string) - 1
    while x < y:
        if string[x] != string[y]:
            return False
        return True


# print(palindromeChecker("akash"))

# Frequency Counter
def frequencyCounter(string):
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


print(frequencyCounter("hello there i am ayush dixit"))
