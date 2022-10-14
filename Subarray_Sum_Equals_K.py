class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        current_sum = 0
        # considering the empty array 0 that has a count of 1
        prefix_sum = {0: 1}
        for i in nums:
            current_sum += i
            d = current_sum - k
            
            result += prefix_sum.get(d,0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum,0) + 1
        return result
