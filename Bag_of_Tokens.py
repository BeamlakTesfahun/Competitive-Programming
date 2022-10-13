class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0 
        left = 0
        right = len(tokens) - 1
        # while score is not empty or power is greater than the ith token
        while left <= right and (score or power >= tokens[left] ):
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left +=1
        # if power is not greater than the ith token 
        # gain more points and lose 1 score
            elif left!= right:
                score -= 1
                power += tokens[right]
                right -= 1 
        # when the left and right pointer are pointing at the same token
        # it is going to be the last iteration so losing score doesn't make sense
        # extra points gained don't matter as it's the last iteration
            else:
                break
        return score
