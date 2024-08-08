def count_upper(s):
    vowels = 'AEIOU'
    count = 0
    for i, c in enumerate(s):
        if i % 2 == 0 and c in vowels:
            count += 1
    return count