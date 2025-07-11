#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def merge(nums1, m, nums2, n):
    x = n - 1  # pointer for nums2
    y = m - 1  # pointer for nums1
    for i in range(m + n - 1, -1, -1):
        if x < 0:
            break
        elif y < 0 or nums2[x] >= nums1[y]:
            nums1[i] = nums2[x]
            x -= 1
        else:
            nums1[i] = nums1[y]
            y -= 1
    return nums1
print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(merge(nums1 = [1], m = 1, nums2 = [], n = 0))
print(merge(nums1 = [0], m = 0, nums2 = [1], n = 1))