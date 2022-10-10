class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        dic = {}
        for i in nums:
            if i in dic:
                counter += dic[i]
                dic [i] +=1
            else:
                dic[i] = 1
        return counter
