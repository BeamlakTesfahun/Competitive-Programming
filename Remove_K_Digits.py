class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k>0 and stack and stack[-1] > c:
                k-=1
                stack.pop()
            stack.append(c)
        # for 12335 case
        stack = stack[:len(stack) - k]
        # stack is a list of numbers - convert it to a string
        result = "".join(stack)
        # for "00 -> to int 0" case and if result is empty return 0
        return str(int(result)) if result else "0"
