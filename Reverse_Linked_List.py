class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        # while current is not null 
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous
