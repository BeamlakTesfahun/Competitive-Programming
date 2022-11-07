class Solution(object):
    def kthLargestNumber(self, nums, k):
        sorted_arr = sorted(nums, key= int,reverse = True)
        return sorted_arr[k-1]
