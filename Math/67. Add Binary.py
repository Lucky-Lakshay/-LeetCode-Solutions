#Given two binary strings a and b, return their sum as a binary string.

def addBinary(a, b):
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = []
    
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        result.append(str(total % 2))
        carry = total // 2

    return ''.join(reversed(result))


print(addBinary(a = "11", b = "1"))    
print(addBinary(a = "1010", b = "1011"))    