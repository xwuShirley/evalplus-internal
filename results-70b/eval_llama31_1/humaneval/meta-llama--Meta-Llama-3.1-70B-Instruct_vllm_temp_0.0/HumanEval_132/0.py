def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            if stack and stack[-1] == '[':
                return True
            stack.append(char)
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
    return False