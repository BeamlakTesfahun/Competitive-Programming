# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d_head = ListNode(0) # place holder to attach values of the sum
        carry_num = 0
        current = d_head # pointer of the added values
    # while l1 or l2 are not pointing to NULL. l1 and l2 dont't necessarily have to equal in length
        while l1 or l2:
            # if l1 has a value at that node
            if l1:
                l1_val = l1.val
            # if l1 doesn't have a value and l2 has a value at that node
            else:
                l1_val = 0
                
            # if l2 has a value at that node
            if l2:
                l2_val = l2.val
            # if l2 doesn't have a value and l1 has a value at that node
            else:
                l2_val = 0
            sum1 = l1_val + l2_val + carry_num
           # store the number at the units place of sum 
            current.next = ListNode(sum1 % 10)
            current = current.next
            carry_num = sum1 // 10
            # updating pointers l1 and l2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # for 4 + 6 case
        if carry_num:
            current.next = ListNode(carry_num)
        return d_head.next
        
