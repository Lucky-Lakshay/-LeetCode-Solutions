#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
def twoSum(nums, target):
    seen = dict()
    for i, num in enumerate(nums):
        #enumerate loop through list and give index and value at same time
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i

print(twoSum(nums = [2,7,11,15], target = 9))    
print(twoSum(nums = [3,2,4], target = 6))    
print(twoSum(nums=[3,3], target=6))    