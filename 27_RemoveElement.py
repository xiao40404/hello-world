class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1

        while start <= end:
            if nums[start] == val:
                nums[start] = nums[end]
                end = end-1
            else:
                start += 1
        return start
