# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

def convertToTitle(columnNumber):
    result = ""

    while columnNumber > 0:
        remainder = columnNumber % 26
        if remainder == 0:
            result += 'Z'
            columnNumber = (columnNumber - 1) // 26
        else:
            result += chr(64 + remainder)
            columnNumber = columnNumber // 26

    return result[::-1]

        
print(convertToTitle(columnNumber = 1))
print(convertToTitle(columnNumber = 28))
print(convertToTitle(columnNumber = 701))