def histogram(test):
    test = test.split()
    if not test:
        return {}
    count_dict = {}
    for letter in test:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    max_count = max(count_dict.values())
    return {k: v for k, v in count_dict.items() if v == max_count}