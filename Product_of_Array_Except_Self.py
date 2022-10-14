class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1
        # from left to right
        for pre in range(len(nums)):
            result[pre] = prefix
            prefix *= nums[pre]
        postfix = 1
        # from right to left -> go to the last element by decrementing -1
        for post in range(len(nums)-1,-1,-1):
            # multiplying it with the element that's already in result
            result[post] *= postfix
            postfix *= nums[post]
        return result
