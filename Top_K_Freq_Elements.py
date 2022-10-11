class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using answer as heap
        answer = []
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        for key, value in d.items():
            if len(answer) < k:
                heapq.heappush(answer,[value,key])
            else:
                heapq.heappushpop(answer, [value,key])
        return [key for value,key in answer]
        
