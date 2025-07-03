# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

def isValid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


print(isValid("()"))    
print(isValid("()[]{}"))    
print(isValid("(]"))    
print(isValid("([])"))    