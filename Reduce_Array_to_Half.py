class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d_freq = {}
        for i in arr:
            d_freq[i] = d_freq.get(i,0) + 1
            # sorted(iterable,key,reverse)
        list1 = sorted(d_freq,key= lambda x:d_freq[x], reverse = True)
        sum1 = 0
        counter = 0
        for i in list1:
            sum1+=d_freq[i]
            counter += 1
            if len(arr) - sum1 <= len(arr)//2:
                return counter
