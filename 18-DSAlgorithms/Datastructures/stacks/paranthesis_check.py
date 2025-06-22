def is_valid(string):
    stack = []
    for ch in string:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        else:
            if len(stack) == 0: 
                return "Invalid"
            else:
                s_ch = stack.pop() # s_ch = (
                if (s_ch == '(' and ch != ')') or \
                   (s_ch == '{' and ch != '}') or \
                   (s_ch == '[' and ch != ']'):
                    return "Invalid"
    
    if len(stack) == 0:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    res = is_valid("()")
    print(f"Result for '()' is: {res}")

    res = is_valid("()[]{}")
    print(f"Result for '()[]{{}}' is: {res}")
    
    res = is_valid("(]")
    print(f"Result for '(]' is: {res}")