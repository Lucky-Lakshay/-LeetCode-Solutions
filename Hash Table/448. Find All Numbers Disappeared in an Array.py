#Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

#sol1
# def findDisappearedNumbers(nums):
#     n = len(nums)
#     nums = set(nums)
#     return list(set(range(1, n+1)) - nums)

#sol 2
def findDisappearedNumbers(nums):
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = -abs(nums[index])  # mark as visited

    # Now collect the indices that remain positive
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)

    return result 


print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(findDisappearedNumbers([1,1]))