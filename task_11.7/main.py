# MAIN #

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def sequence_11_7_a(n):
    x = [1]
    for k in range(n):
        next_x = x[k] / factorial(2 * k + 1)
        x.append(next_x)
    return x

def sequence_11_7_b(n):
    x = [0, 1]
    for k in range(2, n + 1):
        next_x = ((-1) ** k) * x[k - 1] / k
        x.append(next_x)
    return x[1:]

def sequence_11_7_c(n):
    x = [1]
    for k in range(n):
        denominator = factorial(k * k + k)
        next_x = ((-1) ** k) * x[k] / denominator
        x.append(next_x)
    return x

def sequence_11_7_d(n):
    x = [1]
    for k in range(n):
        next_x = (k + 1) * x[k] / factorial(k)
        x.append(next_x)
    return x

# Test
print("11.7 a:", sequence_11_7_a(5))
print("11.7 b:", sequence_11_7_b(5))
print("11.7 c:", sequence_11_7_c(5))
print("11.7 d:", sequence_11_7_d(5))
