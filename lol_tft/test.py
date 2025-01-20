import math

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


for i in range(m, m + n):
    nums1[i] = nums2[i - m]
print(sorted(nums1))
