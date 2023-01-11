class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # operators = ['*', '-', '/', '+' ]
        stack = []
        for char in tokens:
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif char == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b)/a))
            elif char == '*':
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(char))
        return stack[-1]
