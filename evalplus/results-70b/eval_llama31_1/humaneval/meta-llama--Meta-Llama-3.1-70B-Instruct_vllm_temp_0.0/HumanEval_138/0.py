def is_equal_to_sum_even(n):
    for a in range(2, n, 2):
        for b in range(a, n, 2):
            for c in range(b, n, 2):
                for d in range(c, n, 2):
                    if a + b + c + d == n:
                        if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
                            return True
    return False