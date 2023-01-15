class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = sorted(nums)
        dic = {}
        result = []
        for i in range(len(n)):
            if n[i] in dic:
                continue
            dic[n[i]] = i
        for i in nums:
            result.append(dic[i])
        return result
