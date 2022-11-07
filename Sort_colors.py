class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            j = i
            while nums[j - 1] > nums[j] and j > 0:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
