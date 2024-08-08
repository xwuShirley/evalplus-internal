def count_nums(arr):
    count = 0
    for num in arr:
        num_str = str(num)
        if num_str[0] == '-':
            num_str = num_str[1:]
        if sum(int(digit) for digit in num_str) > 0:
            count += 1
    return count