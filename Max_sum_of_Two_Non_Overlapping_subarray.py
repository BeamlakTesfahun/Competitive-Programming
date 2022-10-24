class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        sums = [0] * (len(nums) + 1)
        maxfirstLen = 0
        maxsecondLen = 0
        result = 0
        i = 1
        while (i <= len(nums)) :
            sums[i] = nums[i - 1] + sums[i - 1]
            i += 1
        i = firstLen
        while (i <= len(nums) - secondLen) :
            currfirstLen = sums[i] - sums[i - firstLen]
            currsecondLen = sums[i + secondLen] - sums[i]
            maxfirstLen = max(maxfirstLen,currfirstLen)
            result = max(result,currsecondLen + maxfirstLen)
            i += 1
        i = secondLen
        while (i <= len(nums) - firstLen) :
            currsecondLen = sums[i] - sums[i - secondLen]
            currfirstLen = sums[i + firstLen] - sums[i]
            maxsecondLen = max(maxsecondLen,currsecondLen)
            result = max(result,currfirstLen + maxsecondLen)
            i += 1
        return result
