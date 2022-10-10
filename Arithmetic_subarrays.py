class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arith(nums):
            if len(nums) < 2:
                return False
            if len(nums) == 2:
                return True
            dif = nums[1] - nums[0]
            for i in range(1,len(nums)-1):
                if nums[i+1] - nums[i] != dif:
                    return False
            return True
        
        result= []
        for i in range(len(l)):
            b = nums[l[i]:r[i]+1]
            b.sort()
            if is_arith(b):
                result.append(True)
            else:
                result.append(False)
        return result
