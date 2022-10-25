class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == nums.count(1):
            return len(nums) - 1
        count_before_zero = 0
        count_after_zero = 0
        max_count = 0
        for k in range(len(nums) - 1 ):
            if nums[k] != 0:
                count_before_zero += 1
            else:
                for i in range(k+1, len(nums)):
                    if nums[i] != 0:
                        count_after_zero += 1
                    else:
                        break
                max_count = max(max_count, count_before_zero + count_after_zero)
                count_before_zero = 0
                count_after_zero = 0
        return max_count
