def sort_even(l: list):
    even = sorted([x for i, x in enumerate(l) if i % 2 == 0])
    result = []
    even_index = 0
    for i, x in enumerate(l):
        if i % 2 == 0:
            result.append(even[even_index])
            even_index += 1
        else:
            result.append(x)
    return result