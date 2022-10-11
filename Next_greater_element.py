class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        for i in nums2:
# while stack is not empty and the last element of stack is less than the current element
# pop element from stack and add it to dictionary with the current element as its value
            while (stack and stack[-1] < i):
                k = stack.pop()
                d[k] = i
        # if stack is empty append
            stack.append(i)
        return [d.get(i,-1) for i in nums1]
