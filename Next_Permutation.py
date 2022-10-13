class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_ = len(nums)
        if len_ <= 2:
            return nums.reverse()
        pointer_ = len_ - 2
        while pointer_ >= 0 and nums[pointer_] >= nums[pointer_+1]:
            pointer_ -= 1
        # if all combination is exhausted
        if pointer_ == -1:
            return nums.reverse()
        # if the number at pointer is less than the next number (ascending order)
        for n in range(len_ - 1, pointer_, -1):
            if nums[pointer_] < nums[n]:
                nums[pointer_], nums[n] = nums[n], nums[pointer_]
                break
        # already in descending order after the pointer so reversing it is the same as sorting the array
        nums[pointer_+1:] = reversed(nums[pointer_+1:])
