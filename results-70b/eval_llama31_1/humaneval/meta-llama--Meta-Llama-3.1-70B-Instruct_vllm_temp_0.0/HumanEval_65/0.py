def circular_shift(x, shift):
    num_str = str(x)
    num_digits = len(num_str)
    shift = shift % num_digits
    if shift == 0:
        return num_str
    else:
        return num_str[-shift:] + num_str[:-shift]