def compare_one(a, b):
    # Convert both values to float, replacing comma with dot if necessary
    a = float(str(a).replace(',', '.'))
    b = float(str(b).replace(',', '.'))

    # If values are equal, return None
    if a == b:
        return None

    # Return the larger value in its original type
    if a > b:
        return a if isinstance(a, type(a)) else type(a)(a)
    else:
        return b if isinstance(b, type(b)) else type(b)(b)