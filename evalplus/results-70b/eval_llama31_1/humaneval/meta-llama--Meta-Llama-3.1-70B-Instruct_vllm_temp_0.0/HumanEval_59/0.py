def largest_prime_factor(n: int):
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(n, 1, -1):
        if n % i == 0 and is_prime(i):
            return i