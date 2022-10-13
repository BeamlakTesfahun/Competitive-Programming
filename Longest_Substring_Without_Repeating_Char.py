class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_char = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in set_char:
                set_char.remove(s[left])
                left += 1
            set_char.add(s[right])
            # to calculate the length
            result = max(result,right - left + 1)
        return result
