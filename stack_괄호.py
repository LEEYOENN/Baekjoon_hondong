def is_valid_parentheses(s):
    stack = []
    
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in "({[":
            stack.append(char)

        elif char in ")}]":
            if not stack:
                return False
            
            top = stack.pop()

            if pairs[char] != top:
                return False

    return len(stack) == 0