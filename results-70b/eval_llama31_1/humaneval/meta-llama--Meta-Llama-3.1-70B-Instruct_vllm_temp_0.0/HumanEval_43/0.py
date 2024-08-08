def pairs_sum_to_zero(lst):
    seen = set()
    for num in lst:
        if -num in seen and -num != num:
            return True
        seen.add(num)
    return False