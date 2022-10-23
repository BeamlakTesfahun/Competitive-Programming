class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        result,total = 0, 0
        left, right = 0, 0
        while right < len(nums):
            total += nums[right]
            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1
            result = max(result, right - left + 1)
            right += 1
        return result
