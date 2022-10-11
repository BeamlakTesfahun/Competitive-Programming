class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        for i in range (len(s)):
          # push opening character to stack
            if (s[i] == '('):
                st.append(i)
         #Reverse substring after opening till the current character
            elif (s[i] == ')'):
                temp = s[st[-1]: i + 1]
                s = s[:st[-1]] + temp[::-1] + s[i+1:]
                del st[-1]
        # storing modified string
        res = ""
        for i in range(len(s)):
            if (s[i] != ')' and s[i] != '('):
                res += s[i]
        return res
