class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        result = 0
        for i in nums:
            target = k - i
            if target in dic and dic[target] > 0:
                result += 1
                dic[target] -= 1
            else:
                dic[i] = dic.get(i,0) + 1
        return result
