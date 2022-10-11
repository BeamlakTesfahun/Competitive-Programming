class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch not in "+-/*":
                stack.append(int(ch))
            else:
                r = stack.pop()
                l = stack.pop()
                
                if ch == "*":
                    stack.append(l*r)
                elif ch == "+":
                    stack.append(l+r)
                elif ch == "/":
                    stack.append(int(float(l)/r))
                elif ch == "-":
                    stack.append(l-r)
        return stack[-1]
