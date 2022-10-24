# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is null or there's only one element in the list 
        if not head or not head.next:
            return head
        # split the list into two halves
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        right = temp
        
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
    def getMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, left, right):
        merged_list = dummy = ListNode()
        while left and right:
            if left.val < right.val:
                merged_list.next = left
                left = left.next
            else:
                merged_list.next = right
                right = right.next
            merged_list = merged_list.next
        # if there are remaining elements in the left list and the right list
        if left:
            merged_list.next = left
        if right:
            merged_list.next = right
        return dummy.next
