class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {")" : "(", "]" : "[", "}" : "{"}
        for c in s:
            if c in p:
                # if stack is not empty and last element of the stack is same as p[c]
                if stack and stack[-1] == p[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
    # if stack is empty return true otherwise return false
        return True if not stack else False
