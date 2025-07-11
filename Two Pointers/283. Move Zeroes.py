#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Note that you must do this in-place without making a copy of the array.

def moveZeroes(nums):
    p = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[p] = nums[i]
            p += 1
    for i in range(p, len(nums)):
        nums[i] = 0
    print(nums)


moveZeroes([0,1,0,3,12])
moveZeroes([0])