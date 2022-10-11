class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decQ = collections.deque() #stores max candiadates
        incQ = collections.deque()  #stores min candiadates
        
        answer = 0
        left = 0 
        for right, num in enumerate(nums):
            while decQ and num > decQ[-1]:
                decQ.pop()
                
            decQ.append(num)
            
            while incQ and num < incQ[-1]:
                incQ.pop()
                
            incQ.append(num)
            
            while decQ[0] - incQ[0] > limit:
                if decQ[0] == nums[left]:
                    decQ.popleft()
                    
                if incQ[0] == nums[left]:
                    incQ.popleft()
                    
                left += 1
            answer = max(answer, right - left + 1)
        return answer
