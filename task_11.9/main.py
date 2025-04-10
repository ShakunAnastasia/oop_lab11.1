# MAIN #

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def product_11_9_a(n):
    result = 1
    for i in range(2, n + 1):
        result *= (1 - 1 / (i ** 2))
    return result

def product_11_9_b(n):
    result = 1
    for i in range(1, n + 1):
        result *= (2 + 1 / factorial(i))
    return result

def product_11_9_c(n):
    result = 1
    for i in range(1, n + 1):
        result *= (i + 1) / (i + 2)
    return result

# Test

print("11.9 a:", product_11_9_a(5))
print("11.9 b:", product_11_9_b(5))
print("11.9 c:", product_11_9_c(5))
