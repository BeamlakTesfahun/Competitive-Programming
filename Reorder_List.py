class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle of the linked list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half of the linked list
        prev = None
        second = slow.next
        slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # merge two halves
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
