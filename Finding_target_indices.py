class Solution(object):
    def targetIndices(self, nums, target):
        nums = sorted(nums)
        tArr= []
        for i in range(len(nums)):
            if target == nums[i]:
                tArr.append(i)
        return(tArr)
