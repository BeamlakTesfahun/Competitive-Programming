class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def f(k):
            result = left = right = count_odd = 0
            while right < len(nums):
                count_odd += nums[right] % 2
                while count_odd > k:
                    count_odd -= nums[left] % 2 
                    left += 1
                result += right - left + 1
                right += 1
            return result
        return f(k) - f(k-1)
