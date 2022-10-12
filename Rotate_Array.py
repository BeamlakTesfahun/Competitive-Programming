class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k could be greter than the length of the array
        # if k is the exact length of the array, it's gonna be reversed 0 times
        k = k % len(nums)
        # reversing the entire array
        left , right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] =  nums[right], nums[left]
            left +=1
            right -=1
        # reversing the first kth elements
        left , right = 0, k - 1
        while left < right:
            nums[left], nums[right] =  nums[right], nums[left]
            left +=1
            right -=1
        # reversing the remaining elements
        left , right = k, len(nums) - 1
        while left < right:
            nums[left], nums[right] =  nums[right], nums[left]
            left +=1
            right -=1
