#Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

def titleToNumber(columnTitle):
    result = 0
    for char in columnTitle:
        result = result * 26 + (ord(char) - 64)
    return result

print(titleToNumber(columnTitle = "A"))    
print(titleToNumber(columnTitle = "AB"))    
print(titleToNumber(columnTitle = "ZY"))    