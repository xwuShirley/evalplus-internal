def make_a_pile(n):
    pile = [n]
    next_odd = n + 2
    next_even = n + 1
    for _ in range(n - 1):
        if n % 2 == 0:
            pile.append(next_odd)
            next_odd += 2
        else:
            pile.append(next_even)
            next_even += 2
    return pile