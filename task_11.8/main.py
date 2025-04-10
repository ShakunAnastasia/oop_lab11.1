# MAIN #

def sum_11_8_a(n):
    return sum((-1) ** (k + 1) * k for k in range(1, n + 1))

def sum_11_8_b(n):
    return sum(1 / (k * (k + 1)) for k in range(1, n))

def sum_11_8_c(n):
    return sum(((-1) ** k) * (k - 1) / k for k in range(2, n + 1))

# Test

print("11.8 a:", sum_11_8_a(5))
print("11.8 b:", sum_11_8_b(5))
print("11.8 c:", sum_11_8_c(5))
