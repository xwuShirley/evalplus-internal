def largest_smallest_integers(lst):
    negative = [i for i in lst if i < 0]
    positive = [i for i in lst if i > 0]
    
    if negative:
        a = max(negative)
    else:
        a = None
        
    if positive:
        b = min(positive)
    else:
        b = None
        
    return a, b