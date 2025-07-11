#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
def searchInsert(nums, target):
        k = 0
        for i in range(len(nums)):
            if nums[i] < target:
                k+=1
        return k

print(searchInsert(nums = [1,3,5,6], target = 5))
print(searchInsert(nums = [1,3,5,6], target = 7))
