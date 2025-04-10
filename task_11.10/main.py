# MAIN #

def continued_fraction_11_10(n):
    result = 4 * n + 2
    for i in range(n - 1, 0, -1):
        result = 4 * i + 2 + 1 / result
    return 2 + 1 / result


# Test

print("11.10:", continued_fraction_11_10(5))
