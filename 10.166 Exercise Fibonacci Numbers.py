# Fibonacci Numbers - Adding the first 2 numbers with the next one and so on
# Numbers add up to become very large very quickly
    # F0  F1  F2  F3  F4  F5  F6
    # 0   1   1   2   3   5   8

# Exercise - THIS IS A COMMON INTERVIEW QUESTION
# Create a set of Fibonacci numbers up tp the 20th value using a generator and list

# 1)  This is how we do it using a generator
# This method is faster and keeps nothing in computer memory
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(20):
    print(x)


# 2)  This is how we do it using a list
# This method is slower and takes up computer memory
def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fib2(20))