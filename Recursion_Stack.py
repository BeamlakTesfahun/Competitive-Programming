class Solution:
    def decodeString(self, s: str) -> str:
        stack = [["",1]]
        # list of integers from 0 to 9
        nums = [str(x) for x in range(10)]
        # a string to store the integer values we encounter
        n = ""
        for ch in s:
            if ch in nums:
                n +=ch
            elif ch == "[":
                stack.append(["",int(n)])
                n = ""
            elif ch == "]":
                stack_str, stack_repeat = stack.pop()
                stack[-1][0] += stack_str * stack_repeat
            else:
                stack[-1][0] += ch
        return stack[-1][0]
