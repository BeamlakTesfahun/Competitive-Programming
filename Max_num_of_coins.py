class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        self.quick_sort(piles, 0, len(piles) - 1)
        # 1 2 2 4 7 8 
        alice = len(piles) - 1
        bob = 0
        me = alice - 1
        result = 0
        while alice > bob:
            result += piles[me]
            alice -= 2
            bob += 1
            me = alice - 1
        return result
    def quick_sort(self, piles, left, right):
        if left < right:
            partition_pos = self.partition(piles,left,right)
            self.quick_sort(piles, left, partition_pos - 1)
            self.quick_sort(piles, partition_pos + 1, right)
    def partition(self, piles, left, right):
        i = left
        j = right - 1
        pivot = piles[right]
        while i < j:
            while i < right and piles[i] < pivot:
                i += 1
            while j > left and piles[j] >= pivot:
                j -= 1
            if i < j:
                piles[i], piles[j] = piles[j], piles[i]
        if piles[i] > pivot:
            piles[i], piles[right] = piles[right], piles[i]
        return i
