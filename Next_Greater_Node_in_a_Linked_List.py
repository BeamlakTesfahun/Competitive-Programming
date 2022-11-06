# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        position = -1
        answer = []
        stack = []
        while head:
            position += 1
            answer.append(0)
            while stack and stack[-1][1] < head.val:
                pos, val = stack.pop()
                answer[pos] = head.val
            stack.append((position, head.val))
            head = head.next
        return answer
