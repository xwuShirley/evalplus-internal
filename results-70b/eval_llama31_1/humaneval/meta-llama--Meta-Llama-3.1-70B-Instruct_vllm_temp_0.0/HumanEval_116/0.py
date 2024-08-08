def sort_array(arr):
    return sorted(arr, key=lambda x: (x < 0, bin(abs(x)).count('1'), abs(x)))