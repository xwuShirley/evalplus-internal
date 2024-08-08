def sort_third(l: list):
    third_elements = [l[i] for i in range(len(l)) if i % 3 == 0]
    third_elements.sort()
    for i in range(len(l)):
        if i % 3 == 0:
            l[i] = third_elements.pop(0)
    return l