class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        #outer loop to check if current is not NULL- determines where the current pointer is 
        #inner loop to check if a next node even exists and if values are equal- takes care of the duplicates
        while current:
            while current.next and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        return head
