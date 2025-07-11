#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits.

def plusOne(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] <= 8:
            digits[i] +=1
            break
        else:
            digits[i] = 0
            
    if digits[0] == 0:
        return [1]+digits
    else:
        return digits     

print(plusOne(digits = [1,2,3]))
print(plusOne(digits = [4,3,2,1]))
print(plusOne(digits = [9]))