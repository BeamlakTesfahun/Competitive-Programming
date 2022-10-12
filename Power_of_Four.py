class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        if num <= 0: return False
        if num & num -1 != 0: return False
        b = bin(num)[::-1]
        p = b.index("1")
        return p % 2 == 0
        """
        x = 1
        i = 0
        if n<=0:
            return False
        while x<=n:
            if x == n:
                return True
            i+=1
            x = 4**i
        return False
