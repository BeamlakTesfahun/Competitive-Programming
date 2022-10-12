class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        mx= 3**19
        return n>0 and mx%n==0
        """
        x = 1
        i = 0
        if n<=0:
            return False
        while x<=n:
            if x == n:
                return True
            i+=1
            x = 3**i
        return False
