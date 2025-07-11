#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

def Remove_duplicate(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
    
print(Remove_duplicate(nums = [3,2,2,3], val = 3))
print(Remove_duplicate(nums = [0,1,2,2,3,0,4,2], val = 2))
