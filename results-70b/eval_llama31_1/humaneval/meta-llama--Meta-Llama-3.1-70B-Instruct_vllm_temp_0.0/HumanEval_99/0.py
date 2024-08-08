def closest_integer(value):
    num = float(value)
    if num - int(num) == 0.5:
        return int(num) + (1 if num > 0 else -1)
    else:
        return round(num)