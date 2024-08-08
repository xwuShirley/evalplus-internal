def search(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    result = -1
    for num, freq in count_dict.items():
        if freq >= num:
            if result == -1 or num > result:
                result = num
    return result