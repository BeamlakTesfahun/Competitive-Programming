# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums= []
        while head:
            nums.append(head.val)
            head = head.next
        left = 0
        right = len(nums) - 1
        max_sum = 0
        while left < right:
            max_sum = max(max_sum, nums[left] + nums[right])
            left += 1
            right -= 1
        return max_sum
