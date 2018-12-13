class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cursum = nums[0]
        maxsum = nums[0]
        for num in nums[1:]:
            cursum = max(num,cursum+num)
            maxsum = max(maxsum,cursum)
        return maxsum
