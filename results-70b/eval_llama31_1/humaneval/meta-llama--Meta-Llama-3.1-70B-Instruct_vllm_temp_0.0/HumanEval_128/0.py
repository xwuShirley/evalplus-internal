def prod_signs(arr):
    if not arr:
        return None
    sum_magnitudes = 0
    prod_signs = 1
    for num in arr:
        sum_magnitudes += abs(num)
        if num > 0:
            prod_signs *= 1
        elif num < 0:
            prod_signs *= -1
        else:
            prod_signs *= 0
    return sum_magnitudes * prod_signs