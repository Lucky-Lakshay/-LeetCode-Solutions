# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

def summaryRanges(nums):
    output = []
    start = nums[0]
    for i in range(len(nums)):
        if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
            if start == nums[i]:
                output.append(f"{start}")
            else:
                output.append(f"{start}->{nums[i]}")        
            if i < len(nums) - 1:
                start = nums[i + 1]
    return output
print(summaryRanges(nums = [0,1,2,4,5,7]))
print(summaryRanges(nums = [0,2,3,4,6,8,9]))