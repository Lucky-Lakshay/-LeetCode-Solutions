#Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

def thirdMax(nums):
    nums = set(nums)
    if len(nums) < 3:
        return max(nums)
    else:
        f = s = t = float("-inf") #  -infinity
        for i in nums:
            if i > f:
                f, s, t = i, f, s
            elif i > s:
                s , t = i, s
            elif i > t:
                t = i
        return t              
print(thirdMax([3,2,1]))
print(thirdMax([1,2]))
print(thirdMax([2,2,3,1]))