def correct_bracketing(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if stack and stack[-1] == "<":
                stack.pop()
            else:
                return False
    return not stack