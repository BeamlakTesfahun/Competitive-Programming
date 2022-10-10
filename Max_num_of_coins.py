class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        q = collections.deque(piles)
        
        count =0
        while len(q)>0:
            q.popleft()
            q.pop()
            count += q[-1]
            q.pop()
            
        return count
