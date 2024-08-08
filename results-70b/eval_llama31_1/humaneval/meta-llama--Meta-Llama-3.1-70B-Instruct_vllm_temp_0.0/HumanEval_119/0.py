def match_parens(lst):
    s1 = lst[0]
    s2 = lst[1]
    
    # Count the total number of open and close parentheses
    open_parens = s1.count('(') + s2.count('(')
    close_parens = s1.count(')') + s2.count(')')
    
    # If the total number of open and close parentheses are not equal, 
    # it's impossible to make a good string
    if open_parens != close_parens:
        return 'No'
    
    # Initialize variables to keep track of the balance of parentheses
    balance1 = 0
    balance2 = 0
    
    # Check if the strings are already good
    for char in s1:
        if char == '(':
            balance1 += 1
        else:
            balance1 -= 1
        if balance1 < 0:
            break
    else:
        return 'Yes'
        
    for char in s2:
        if char == '(':
            balance2 += 1
        else:
            balance2 -= 1
        if balance2 < 0:
            break
    else:
        return 'Yes'
        
    # If the strings are not already good, check if concatenating them in 
    # reverse order makes a good string
    for char in s1 + s2[::-1]:
        if char == '(':
            balance1 += 1
        else:
            balance1 -= 1
        if balance1 < 0:
            break
    else:
        return 'Yes'
        
    for char in s2 + s1[::-1]:
        if char == '(':
            balance2 += 1
        else:
            balance2 -= 1
        if balance2 < 0:
            break
    else:
        return 'Yes'
        
    # If none of the above checks pass, return 'No'
    return 'No'