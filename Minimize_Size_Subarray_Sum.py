class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total_sum = 0, 0
        # since the length has to be minimized, set result to a large number
        result = len(nums) + 1
        for right in range(len(nums)):
            total_sum += nums[right] 
            while total_sum >= target:
                result = min(result, right - left + 1)
                total_sum -= nums[left]
                left += 1   
        return 0 if result == len(nums) + 1 else result
        
