class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # if  there is no True for. (if input = [0,0] Output becomes "00" otherwise) 
        if not any(map(bool,nums)):
            return '0'
        nums = list(map(str,nums))
        if len(nums)<2:
            return "".join(nums)
        
        def compare(x,y):
            return int(nums[x] + nums[y]) > int(nums[y] + nums[x])
        
        for x in range(len(nums)-1):
            y = x + 1
            while x < len(nums) and y< len(nums):
                if compare(x,y):
                    pass
                else:
                    nums[y],nums[x] = nums[x],nums[y]
                y += 1
        return "".join(nums)
