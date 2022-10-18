class Solution(object):
    def maxScore(self, cardPoints, k):
        left = 0
        right = len(cardPoints) - k
        total_sum = sum(cardPoints[right:])
        result = total_sum
        
        while right < len(cardPoints):
            total_sum += (cardPoints[left] - cardPoints[right] )
            result = max(result,total_sum)
            left += 1
            right += 1
        return result
