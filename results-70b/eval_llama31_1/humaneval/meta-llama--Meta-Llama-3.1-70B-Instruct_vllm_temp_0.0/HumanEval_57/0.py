def monotonic(l: list):
    increasing = decreasing = True
    
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            increasing = False
        if l[i] < l[i + 1]:
            decreasing = False
    
    return increasing or decreasing