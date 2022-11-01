class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack, current_num, operator = [], 0, "+"
        operators = {"+", "-", "/", "*"}
        numbers = set((str(i) for i in range(10)))
        for i in range(len(s)):
            if s[i] in numbers:
                current_num = current_num * 10 + int(s[i])
            if s[i] in operators or i == len(s) -1: 
                if operator == "+":
                    stack.append(current_num)
                elif operator == "-":
                    stack.append(-current_num)
                elif operator == "*":
                    stack[-1] *= current_num
                elif operator == "/":
                    stack[-1] = int(stack[-1] / current_num)
                current_num = 0
                operator = s[i]
        return sum(stack)
