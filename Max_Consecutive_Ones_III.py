class Solution:
    #?
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_ = 0
        for right, n in enumerate(nums):
            # doesn't decrease the value of k if the number is 1
            k -= 1-n
            if k < 0:
                k +=(1-nums[left])
                left += 1
            max_ = max(max_,right - left + 1)
        return max_
