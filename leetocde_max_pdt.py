# Leet code
# find the maximum product
# [3,1,4,3] sort , max* next smalles* next smallest
# if negative [max val ie -1 , smallest [0] next smallest[-1]
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return (max(nums[-3]*nums[-2]*nums[-1],nums[-1]*nums[0]*nums[1]))
