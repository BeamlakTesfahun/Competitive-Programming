class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1
            
        answer = 0
        for i in nums:
            if k//2 == i and k%2==0:
                value = min(count[i],count[k-i])
                answer += value // 2
                count[i] = 0
                count[k-i] = 0
            elif count[i] != 0:
                if k-i in count and count[k-i] != 0:
                    answer += 1
                    count[k-i] -= 1
                    count[i] -=1
        return answer
