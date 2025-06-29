#Given a binary array nums, return the maximum number of consecutive 1's in the array.

def findMaxConsecutiveOnes(nums):
    m = 0
    x = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            x+=1
            if x > m:
                m = x  
        else:   
            x=0   
    return m
    
print(findMaxConsecutiveOnes([1,1,0,1,1,1]))    
print(findMaxConsecutiveOnes([1,0,1,1,0,1]))    