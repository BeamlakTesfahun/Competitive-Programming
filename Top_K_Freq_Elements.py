class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        result = []
        for i in nums:
            dic[i] = dic.get(i,0) + 1
            # sorted(iterable,key,reverse)
        #print(dic)
        list1 = sorted(dic,key= lambda x:dic[x])
        print(list1)
        while k > 0:
            result.append(list1.pop()) 
            k -= 1
        return result
        
