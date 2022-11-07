class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        result = [] 
        answer = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            result.append([dist, x, y])
        result = sorted(result, key = lambda x: x[0], reverse = True)
        print(result)
        while k > 0:
            dist, x, y = result.pop()
            answer.append([x,y])
            k -= 1
        return answer
