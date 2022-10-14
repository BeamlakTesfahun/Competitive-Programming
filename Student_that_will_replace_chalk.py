class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum1 = sum(chalk)
        max1 = k%sum1
        current = chalk[0]
        i = 0
        while (i < len(chalk)):
            if max1 - chalk[i] >= 0:
                max1-= chalk[i]
            else:
                return i
            i+=1
        return i
