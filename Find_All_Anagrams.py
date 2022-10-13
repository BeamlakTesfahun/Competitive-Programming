class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
       # if the length of p is greater than the string there could be anagram
        if len(p) > len(s):
            return []
        p_counter = {}
        s_counter = {}
        for i in range (len(p)):
            p_counter[p[i]] = p_counter.get(p[i],0) + 1
            s_counter[s[i]] = s_counter.get(s[i], 0) + 1
        result = [0] if s_counter == p_counter else []
        left = 0
        # the first string is already compared
        for right in range(len(p), len(s)):
            s_counter[s[right]] = s_counter.get(s[right] , 0) + 1
            s_counter[s[left]] -= 1
            
            if s_counter[s[left]] == 0:
                s_counter.pop(s[left])
            left += 1
            if s_counter == p_counter:
                result.append(left)
        return result
            
