def smallest_change(arr):
    left, right = 0, len(arr) - 1
    changes = 0
    
    while left < right:
        if arr[left] != arr[right]:
            changes += 1
        left += 1
        right -= 1
    
    return changes