class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        if time == 0:
            return list(range(len(security)))
        left = [1]
        right = [1]
        n = len(security)
        # non-increasing on the left side
        current = 1
        for i in range(1,n):
            if security[i] <= security[i-1]:
                current += 1
            else:
                current = 1
            left.append(current)
        # non decreasing on the right side
        current = 1
        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                current += 1
            else: 
                current = 1
            right.append(current)
        right.reverse()
        return [i for i in range(n) if left[i] >= time + 1 and right[i] >= time + 1]
